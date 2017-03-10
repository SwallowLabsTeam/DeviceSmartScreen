import json
import subprocess

class ReposiotyHandler:
    
    def __init__(self):
        pass

    def book_segment(self,res_dict):
        global ACKK
        ACKK = True
        for j in res_dict["pakage_name"]:
            commade_exec = "yum -y " + res_dict["action"] +" "+j
            print(commade_exec)
            #os.system(commade_exec+" &>> /root/test/test1.txt")
            x=self.verif_exist(commade_exec)
            print("xxxxxxxxxxxxx ",x)
            if(x>0):
                ACKK=False
                break;
            
        
        return ACKK
      

    def verif_exist(self,cmd):
        #cmd = "yum install aaaaa"
        print("aaaaaaaaaaaaaa",cmd)  
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                              stderr=subprocess.STDOUT, close_fds=True)
        output = p.stdout.read()
        
        #os.system(cmd)
        print("aaaaaaaaaaaaaa",output)  
        str1 = str(output)
        print("aaaaaaaaaaaaaa",str1) 
        nn = str1.find("Aucun paquet")
        print(nn)
        return nn
    
    
    def book_multiple_segment(self,res_dict):
        for i in res_dict:
            self.book_segment(i)
        return ACKK


    def generate_res_dict(self,reservation_msg_queue):
        json_data = []
        for i in reservation_msg_queue:
            json_data.append(i.get_payload())
        return json_data


