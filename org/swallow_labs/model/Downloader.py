import paramiko
import json
from pprint import pprint
import time
import datetime


from tempfile import mkstemp
from shutil import move

import os
from DeleteGenerator import DeleteGenerator





class Downloader:
    @staticmethod
    def download_file(file_name, local_path):
        with open("../conf/Configuration_Display.json") as json_data:
            config = json.load(json_data)
            json_data.close()
        host = config["sftp"]["host"]
        port = 22
        transport = paramiko.Transport((host, port))
        private_key_path = config["sftp"]["private_key_path"]
        username = config["sftp"]["username"]
        with open(private_key_path) as file_object:
            print(file_object)
            mykey = paramiko.RSAKey.from_private_key(file_object)
            file_object.close()
        transport.connect(pkey=mykey, username=username)

        sftp = paramiko.SFTPClient.from_transport(transport)
        null, file_extension = file_name.split(".")
        if file_extension in config["video_extension"]:
            file_path = config["sftp"]["video_directory"] + file_name
        else:
            file_path = config["sftp"]["photo_directory"] + file_name

        local_path += file_name
        print("localpath = ", local_path)
        print("file_path = ", file_path)
        sftp.get(file_path, local_path)
        sftp.close()
        transport.close()

    @staticmethod
    def download_day(planning_directory):
        with open(planning_directory + "/Planning.json", "r") as json_data:
            planning = json.load(json_data)
            json_data.close()
        for i in planning["planning"]["heure"]:
            for j in i["creneau"]:
                path = planning_directory + i["id"] + "/" + j["id"] + "/"
                print('path: ',path)
                print("video:: ",j["video"]["id"])
                print("photo:: ",j["photo"]["id"])
                video=j["video"]["id"]
                photo = j["photo"]["id"]
                if(video!=""):
                    Downloader.download_file(j["video"]["id"], path)
                if(photo!=""):
                    Downloader.download_file(j["photo"]["id"], path)
                    #Downloader.download_file(j["photo"]["id"], path)
    @staticmethod
    def change_planing_crontab(dd):
        with open(dd+'/Planning.json') as data_file:    
            data = json.load(data_file)
        pprint(data["planning"]["segment_duration_min"])
        #os.system( "crontab -l > /root/test/crontabtime.txt")
        file_path= "/var/spool/cron/root"
        f = open(file_path, 'r+b')   
        f_content = f.read()
        f.close()
        
        
        print("aaaaaaaaaaaaaa",f_content)  
        str1 = str(f_content)
        print("aaaaaaaaaaaaaa",str1) 
        nn = str1.find("/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt")
        print(nn)
        old1= str1[nn-14 : nn-10]
        print("timea:",old1)
        
        
        old =old1+" * * * *\t/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt"
        print("timea:",old)
        new ="*/"+data["planning"]["segment_duration_min"]+" * * * *\t/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt"
        print("new:",new)
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(old, new))
        os.close(fh)
        #Remove original file
        os.remove(file_path)
        #Move new file
        move(abs_path, file_path)
        os.system("systemctl restart crond")
        
if __name__ == '__main__':
    
    deleting = DeleteGenerator()
    deleting.__init__()
   
    
    print (time.strftime("%H:%M:%S"))
    print (time.strftime("%d/%m/%Y"))
    
    i = datetime.datetime.now()
     
    print (i.year)
    print (i.month)
    print (i.day)
    print (i.hour)
    heur = i.hour
    #print ("miiiiiiiiiiii",i.minute//10*10)
    creneau = (i.minute//10*10)//10
    #print ("dddddddddddd",creneau)
    #print (i.second)
    if(i.month<10):
        monthstr="0"+str(i.month)
    else:
        monthstr=str(i.month)
    
    if(i.day<10):
        daystr="0"+str(i.day)
    else:
        daystr=str(i.day)
                
    dd ="/reservation/"+str(i.year)+"/"+monthstr+"/"+daystr
    print(dd)
    
    Downloader.change_planing_crontab(dd)
        
    
    folder_day=dd+"/"
    print ("folder_day",folder_day)
    #Downloader.download_day("/reservation/2017/02/03/")
    Downloader.download_day(folder_day)
    #Downloader.download_file("swallow-video.mp4", "/reservation/2016/09/07/00/10/")

