from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
from org.swallow_labs.model.LdapParam import *
import os
import json
from calendar import monthrange
from org.swallow_labs.model.Client import *
from org.swallow_labs.model.CapsuleACK import *
from org.swallow_labs.tool.CapsulePriority import *
import org.swallow_labs.model.RunClient
import org.swallow_labs.model.SocketClient
import org.swallow_labs.model.ReservationHandler
from subprocess import *
from org.swallow_labs.model.TreeGenerator import *
from org.swallow_labs.model.ReservationHandler import *

class CapsuleProcessor:

    """
        Class creating a CapsuleProcessor object
        G{classtree}
        DESCRIPTION
        ===========
        Class that treat capsule

        @param cpl    : The capsule that will be treated


        @type cpl     : Capsule

    """
    ldap_param = LdapParam()
    # load ldap connexion param
    list_capsuleACK_all_msg = []
    # list capsuleACK_all_msg

    def __init__(self, cpl):
        """
                   :

        """
        self.cpl = cpl
        # initialize the capsule  that will be treated

    def treat(self,obj_ACK):
        """
        DESCRIPTION
        ===========
        Method that treat a capsule
        """
        if self.cpl.get_sort() == CapsuleSort.LDAP_ADD_MSG:
        # Test the sort of capsule
            self.ladp_add_sendACK(obj_ACK)
            # Run the method that treat the LDAP_ADD_MSG capsule

        elif self.cpl.get_sort() == CapsuleSort.LDAP_MOD_MSG:
        # Test the sort of capsule
            self.ladp_mod_sendACK(obj_ACK)
            # Run the method that treat the LDAP_MOD_MSG capsule

        elif self.cpl.get_sort() == CapsuleSort.LDAP_DEL_MSG:
        # Test the sort of capsule
            self.ladp_del_sendACK(obj_ACK)
            # Run the method that treat the LDAP_DEL_MSG capsule
        elif self.cpl.get_sort() == CapsuleSort.TREE_GENERATOR:
        # Test the sort of capsule
            self.tree_generator()
            # Run the method that treat the LDAP_DEL_MSG capsule
        elif self.cpl.get_sort() == CapsuleSort.RESERVATION_MESSAGE:
        # Test the sort of capsule
            self.reservation()
            # Run the method that treat the LDAP_DEL_MSG capsule

    def verif_msg(self):
        """
        DESCRIPTION
        ===========
        Method that treat a LDAP_ADD_MSG capsule
        """

        id_capACK= self.cpl.get_id_capsule();
        #id for capsule ACK
        print(id_capACK)
        b = False
        print("list:",self.list_capsuleACK_all_msg)
        for h in self.list_capsuleACK_all_msg:
            if h.id_capsule == id_capACK:
                b = True
                obj_ACK = h
        # to verifie existens of capsule in the list of capsuleADD
        result = None
        if(b):
          if(obj_ACK.status == "NO" ):
           #test of the capsule is not treated
                #self.ladp_add_sendACK(obj_ACK)
                result = obj_ACK

        else:
        # new capsule to treat
            obj_capsuleACK = CapsuleACK(id_capACK,"NO")
            self.list_capsuleACK_all_msg.append(obj_capsuleACK)
            # Add capsule Ack status in the status list
           # self.ladp_add_sendACK(obj_capsuleACK)
            result = obj_capsuleACK
            # Do the Ldap-Add process and send ACK
        return result




    def ladp_add_sendACK(self,objACK):

        """
        DESCRIPTION
        ===========
        Method to add ldap new entry and send ACK
        """

        pld = self.cpl.get_payload()
        # Get capsule payload
        add_file = 'ldap_add_file.ldif'
        # Specify the name of file that contain entry information
        self.ldap_file_creator_add(add_file, pld)
        # Creation of the ldap file using capsule payload information
        admin = self.ldap_param.admin
        password = self.ldap_param.password
        # Load ldap param
        cmd = "ldapadd  -h 10.10.10.2  -D " + '"' + str(admin) + '"' + " -w " + password + " -f ./" + str(add_file)
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        # execute the ldap command that will add the new entry in the ldap tree using ldap_add_file.ldif
        output = p.stdout.read()
        str1 = str(output)
        print("str111 ",str1)
        #Load the command output
        if (str1.find('Already exists') > 0):
        # Test if the entry is aleady exist
            f = self.list_capsuleACK_all_msg.index(objACK)
            self.list_capsuleACK_all_msg[f].status = "YES"
            self.sendACK(CapsuleSort.LDAP_ADD_MSG_ACK_NEGATIF, self.cpl.id_capsule, self.cpl.id_sender)
          # send negatif ACk
        elif (str1.find('adding new entry') > 0):

            # Test if the entry is added succeful
            f = self.list_capsuleACK_all_msg.index(objACK)
            self.list_capsuleACK_all_msg[f].status = "YES"
            # Change status capsule Ack
            self.sendACK(CapsuleSort.LDAP_ADD_MSG_ACK_POSITIF, self.cpl.id_capsule, self.cpl.id_sender)
            # send positif ACk
        else:
            self.log_ACK_error(str1)
            # loggin errors

        os.remove("./" + str(add_file))
        # delete ldap_add_file






    def ladp_mod_sendACK(self,objACK):
        """
        DESCRIPTION
        ===========
        Method to add ldap Modify entry and send ACK

        """

        pld = self.cpl.get_payload()
        # Get capsule payload
        mod_file = 'ldap_mod_file.ldif'
        # Specify the name of file that contain the modification information
        self.ldap_file_creator_mod(mod_file, pld)
        # Creation of the ldap file using capsule payload information
        admin = self.ldap_param.admin
        password = self.ldap_param.password
        # Load ldap param
        cmd = "ldapmodify  -h 10.10.10.2  -D " + '"' + str(admin) + '"' + " -w " + password + " -f ./" + str(mod_file)
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        # execute the ldap command that will Modify the entry in the ldap tree using ldap_mod_file.ldif
        output = p.stdout.read()
        str1 = str(output)
        # Load the command output

        if (str1.find('No such object') > 0):
            # Test if the entry is aleady exist
            self.sendACK(CapsuleSort.LDAP_MOD_MSG_ACK_NEGATIF, self.cpl.id_capsule, self.cpl.id_sender)
            #send negatif ACK

        elif (str1.find('modifying entry') > 0):
            # Test if the entry is modify succeful
            f = self.list_capsuleACK_all_msg.index(objACK)
            self.list_capsuleACK_all_msg[f].status = "YES"
            # Change status capsule Ack
            self.sendACK(CapsuleSort.LDAP_MOD_MSG_ACK_POSITIF, self.cpl.id_capsule, self.cpl.id_sender)
            #send positif ACK
        else:
            self.log_ACK_error(str1)
            # loggin errors

        os.remove("./" + str(mod_file))
        # delete ldap_mod_file



    def ladp_del_sendACK(self, objACK):
        """
        DESCRIPTION
        ===========
        Method to add ldap delete entry and send ACK

        """

        pld = self.cpl.get_payload()
        # Get capsule payload
        entry = '"' + str(pld["dn"]) + '"'
        print("entry: ", entry)
        # get the dn of entry that will be deleted
        admin = self.ldap_param.admin
        password = self.ldap_param.password
        # Load ldap param


        cmd = "ldapdelete -h 10.10.10.2 -D " + '"' + str(admin) + '"' + " -w " + password + " -v " + entry
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        # execute the ldap command that will delete the entry in the ldap
        output = p.stdout.read()
        str1 = str(output)
        # Load the command output
        if (str1.find('No such object') > 0):
            # Test if the object is aleady exist
            self.sendACK(CapsuleSort.LDAP_DEL_MSG_ACK_NEGATIF, self.cpl.id_capsule, self.cpl.id_sender)
            # send negatif ACK
        elif(str1.find('eleting entry') > 0):

            # Test if the entry is deleted succeful
            f = self.list_capsuleACK_all_msg.index(objACK)
            self.list_capsuleACK_all_msg[f].status = "YES"
            # Change status capsule Ack
            self.sendACK(CapsuleSort.LDAP_DEL_MSG_ACK_POSITIF, self.cpl.id_capsule, self.cpl.id_sender)
            # send positif ACK
        else:
            self.log_ACK_error(str1)
            # loggin errors

    @staticmethod
    def ldap_file_creator_add(file, pld):

        """
            DESCRIPTION
            ===========
            This method create file that contain ldap entry information
            @param file: the file name
            @param pld: capsule payload that will be copied in the file

            @type file: str
            @type pld : dict
        """
        f = open(file, 'w')
        for h in pld["att"]:
            if type(pld[str(h)]) == list:
                for k in pld[str(h)]:
                    f.write(h + ":" + k + "\n")
            else:
                f.write(str(h) + ':' + str(pld[str(h)]) + "\n")
        # write in the file the capsule payload that contains information about the new ldap entry
        f.close()

    @staticmethod
    def ldap_file_creator_mod(file, pld):

        """
            DESCRIPTION
            ===========
            This method create file that contain ldap entry information
            @param file: the file name
            @param pld: capsule payload that will be copied in the file

            @type file: str
            @type pld : dict
        """
        f = open(file, 'w')
        for h in pld["att"]:
            if type(pld[str(h)]) == list:
                for k in pld[str(h)]:
                    f.write(str(h) + ":" + str(k )+ "\n")
                    f.write(k + ":" + pld[str(k)] + "\n")
                    f.write("-\n")

            else:
                f.write(str(h) + ':' + str(pld[str(h)]) + "\n")
        # write in the file the capsule payload that contains information about the new ldap entry
        f.close()



    def sendACK(self,capsule_sort,id_capsule,id_sender):
        """
            DESCRIPTION
            ===========
            This method will send ack
            @param capsule_sort: the capsule sort
            @param id_sender: The id sender
            @param id_capsule: The id of the capsule

            @type capsule_sort: CapsuleSort
            @type id_sender : int
            @type id_capsule : int
        """

        capsule = Capsule(org.swallow_labs.model.RunClient.client_pull.id_client, CapsuleType.PAYLOAD)
        # initialize capsule
        capsule.set_yes_ACK()
        capsule.set_payload({'id': id_capsule})
        capsule.set_id_receiver(str(id_sender))
        capsule.set_sort(capsule_sort)
        capsule.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
        # Load information in the capsule
        org.swallow_labs.model.RunClient.client_pull.push(capsule)
        # send Capsule

    def log_ACK_error(self, error_msg):
        """
            DESCRIPTION
            ===========
            This method will log treatment error
            @param error_msg: the error message

            @type error_msg: str

        """
        if (error_msg.find('contact LDAP server') > 0):
            print("b1")
            print(error_msg)
            org.swallow_labs.model.SocketClient.my_logger.log_sendACK_error_server_down(str(self.cpl.id_capsule), str(
                org.swallow_labs.model.RunClient.client_pull.id_client))
            # add error log when the LADP server is down
        else:
            if (error_msg.find('not found') > 0):
                print("b2")
                org.swallow_labs.model.SocketClient.my_logger.log_sendACK_error_request(str(self.cpl.id_capsule), str(
                    org.swallow_labs.model.RunClient.client_pull.id_client))
                # add error log when we have an error syntax form the server
            else:
                if (error_msg == 'b\'\''):
                    print("b3")
                    org.swallow_labs.model.SocketClient.my_logger.log_sendACK_error_structure(str(self.cpl.id_capsule),
                                                                                              str(
                                                                                                  org.swallow_labs.model.RunClient.client_pull.id_client))
                    # add error log when we have an error syntax form the web
    
    
    def tree_generator(self):
    
        tree = TreeGenerator()
        print( tree.generate_set_list( tree.generate_list([self.cpl])))
        tree.create_days( tree.generate_set_list( tree.generate_list([self.cpl])))
        
    def reservation(self):
        reserve = ReservationHandler()
        list=[self.cpl.get_payload()]        
        reserve.book_multiple_segment(list)
 
