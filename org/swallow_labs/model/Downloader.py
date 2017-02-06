import paramiko
import json
from pprint import pprint
import time
import datetime


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

if __name__ == '__main__':
    print (time.strftime("%H:%M:%S"))
    print (time.strftime("%d/%m/%Y"))
    
    i = datetime.datetime.now()
     
    print (i.year)
    print (i.month)
    print (i.day)
    print (i.hour)
    print (i.minute//10*10)
    print (i.second)
    
    print ("/reservation/"+str(i.year)+"/"+str(i.month)+"/"+str(i.day)+"/")
    folder_day="/reservation/"+str(i.year)+"/"+str(i.month)+"/"+str(i.day)+"/"
    print("type: ",type(str(int("05"))))
    Downloader.download_day("/reservation/2017/01/17/")
    #Downloader.download_file("swallow-video.mp4", "/reservation/2016/09/07/00/10/")

