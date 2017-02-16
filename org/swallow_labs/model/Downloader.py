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
    """
                DESCRIPTION
                ===========
                This method will download the video and photo file from the sftp server

    
    """
    @staticmethod
    def download_file(file_name, local_path):
        """
                DESCRIPTION
                ===========
                This method download files(video and photo)

    
        """
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
        """
                DESCRIPTION
                ===========
                This method get information file to download it

    
        """
        with open(planning_directory + "/Planning.json", "r") as json_data:
            planning = json.load(json_data)
            json_data.close()
        for i in planning["planning"]["heure"]:
            for j in i["creneau"]:
                path = planning_directory + i["id"] + "/" + j["id"] + "/"
                video=j["video"]["id"]
                photo = j["photo"]["id"]
                if(video!=""):
                    Downloader.download_file(j["video"]["id"], path)
                if(photo!=""):
                    Downloader.download_file(j["photo"]["id"], path)
    @staticmethod
    def change_planing_crontab(dd):
        """
                DESCRIPTION
                ===========
                This method set the time in the line how run loop video and photo

    
        """
        # open planning.json file to get segment_duration_min value
        with open(dd+'/Planning.json') as data_file:    
            data = json.load(data_file)
        #pprint(data["planning"]["segment_duration_min"])
        #set crontab file
        file_path= "/var/spool/cron/root"
        f = open(file_path, 'r+b')   
        f_content = f.read()
        f.close()
        
        str1 = str(f_content)
        #get the line to set it in crontab 
        nn = str1.find("/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt")
        old1= str1[nn-14 : nn-10]
        
        
        old =old1+" * * * *\t/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt"
        new ="*/"+data["planning"]["segment_duration_min"]+" * * * *\t/usr/local/bin/python3.5 /root/test/testaff.py &>> /home/user/testloop.txt"
        print("new:",new)
        fh, abs_path = mkstemp()
        # set the old line in crontab
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
    """
                DESCRIPTION
                ===========
                This method to generate downloader step 

    
    """
    # delete previous date repository
    deleting = DeleteGenerator()
    deleting.__init__()
   
    
    #print (time.strftime("%H:%M:%S"))
    #print (time.strftime("%d/%m/%Y"))
    
    i = datetime.datetime.now()
    heur = i.hour
    # set month forme
    if(i.month<10):
        monthstr="0"+str(i.month)
    else:
        monthstr=str(i.month)
    #set day forme
    if(i.day<10):
        daystr="0"+str(i.day)
    else:
        daystr=str(i.day)
                
    dd ="/reservation/"+str(i.year)+"/"+monthstr+"/"+daystr
    print(dd)
    # chage  execution time crontab  
    Downloader.change_planing_crontab(dd)
        
    
    folder_day=dd+"/"
    #print ("folder_day",folder_day)
    #Downloader.download_day("/reservation/2017/02/03/")
    # download files in folder day
    Downloader.download_day(folder_day)
    #Downloader.download_file("swallow-video.mp4", "/reservation/2016/09/07/00/10/")

