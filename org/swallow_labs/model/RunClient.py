from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.CapsuleProcessor import CapsuleProcessor
from org.swallow_labs.model.BrokerEventManager import *
import org.swallow_labs.model.SendProcessor

from multiprocessing import Process, Manager
from org.swallow_labs.model.Capsule import *
class RunClient:
    """
        Class creating a RunClient object
        G{classtree}
        DESCRIPTION
        ===========
        Class that launches a Client in a routine

        @:param id_client         : a client id
        @:param list_address      : List of ip address and ports of the host the client is connecting to
        @:param client_pull       : the client stub for pull
        @:param client_push       : the client stub for push
        @:param shared_dict       : list of item capsules

        @:type id_client          : int
        @:type list_address       : list
        @:type client_pull        : Client
        @:type client_push        : Client
        @:type shared_dict        : dict

    """

    def __init__(self, id_client,id_client_push,id_event):

        """
            DESCRIPTION
        ===========

        """

        self.id_client = id_client
        self.id_event = id_event
        self.id_client_push = id_client_push
        self.list_address = Parser.get_backend_broker_list()
        # Load global client param
        manager = Manager()
        #control process objects
        global shared_dict
        shared_dict = manager.dict()
        #dic how shared memory
        shared_dict['list_item'] = list()
        #list of items dec shared

        self.event=BrokerEventManager(self.id_event)
        global client_pull
        client_pull = Client(self.id_client, self.list_address)
        global client_push
        client_push = Client(self.id_client_push, self.list_address)
        client_push.generate()
        # instantiate a Client
        p = Process(target=self.pull_routine)
        p.start()
        p1 = Process(target=self.push_routine())
        time.sleep(0.01)
        p1.start()
        time.sleep(0.01)
        # launch the routine method in a process

    def push_routine(self):
        self.event.start(client_push)

    def remove_capsule(self,cap):
        """
        DESCRIPTION
        ===========
        Method that remove capsule using id

         """
        item = shared_dict['list_item']
        #add list item in item
        item.pop(cap)
        # remove capsule from item with position
        shared_dict['list_item'] = item
        #refresh list item with new list item
        print('main process:', shared_dict['list_item'])



    def pull_routine(self):

         """
        DESCRIPTION
        ===========
        Method that run a client stub and pull capsule in loop

         """

         client_pull.generate()
         while (True):
             # loop for pull
             client_pull.pull()
             # client pull
             for x in client_pull.pull_list:
                 if(x.get_ACK()=="YES"):
                     pld=x.get_payload()
                     print(x.print_capsule())
                     #get payload capsule
                     for i in  range(len(shared_dict['list_item'])):
                         print("liste capsule",shared_dict['list_item'][i].get_id_capsule())
                         #print capsule remove
                         if(shared_dict['list_item'][i].get_id_capsule()==pld["id"]):
                             self.remove_capsule(i)
                             #remove capsule after verification payload
                     client_pull.pull_list.pop(0)
                     # pop the treated capsule from the pull_list
                 else:
                     t = CapsuleProcessor(x)
                     # instantiate a CapsuleProcessor that will treat capsule
                     y = t.verif_msg()
                     if (y == None):
                         print('capsule verif false')
                         org.swallow_labs.model.SocketClient.my_logger.log_sendACK_verif(
                             str(x.id_capsule), str(
                                 client_pull.id_client))
                         client_pull.pull_list.pop(0)
                         # pop the treated capsule from the pull_list
                     else:
                         t.treat(y)
                         #treat capsule
                     x.my_logger.log_treated_capsule(x)
                     # log that the capsule was treated
                     client_pull.pull_list.pop(0)
                     # pop the treated capsule from the pull_list
             time.sleep(3)
             print("list: ", shared_dict['list_item'])
             for hd in shared_dict['list_item']:
                 print(hd.print_capsule())
                 #print capsules in list item








