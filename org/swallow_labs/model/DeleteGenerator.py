from tempfile import mkstemp
from shutil import move

import time
import subprocess
import datetime

import json
from pprint import pprint

import json
import os
from calendar import monthrange
from Capsule import Capsule
import shutil


class DeleteGenerator:
    @staticmethod
    def delete_day(date):
        print(date)
        year, month, day = date.split("-")
        with open("../conf/Configuration_Display.json") as json_config:
            config = json.load(json_config)
            json_config.close()
        if not os.path.exists(config['reservation_root_directory'] + "/" + str(year)+ "/" + str(month) + "/" + str(day)):
            print("goood month")
        else:
            print("dellleeeeteee", config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day))
            
            
            shutil.rmtree(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day))
           
    @staticmethod
    def delete_month(month,year):
        print(month)
        
        with open('Configuration_Display.json') as json_config:
            config = json.load(json_config)
            json_config.close()
            
        
            
        print("mmmmmmm" +month)
            
        if not os.path.exists(config['reservation_root_directory'] + "/" + str(year)+ "/" + month ):
            print("goood month")
        else:
            print("dellleeeeteee", config['reservation_root_directory'] + "/" + str(year) + "/" + month )
            shutil.rmtree(config['reservation_root_directory'] + "/" + str(year) + "/" + month  )
        
    @staticmethod
    def delete_year(year):
        print(year)
        
        with open("../conf/Configuration_Display.json") as json_config:
            config = json.load(json_config)
            json_config.close()
            
       
        if not os.path.exists(config['reservation_root_directory'] + "/" + str(year)):
            print("goood year")
        else:
           
            print("dellleeeeteee", config['reservation_root_directory'] + "/" + str(year)  )
            
            
            shutil.rmtree(config['reservation_root_directory'] + "/" + str(year) )
            
    
    @staticmethod
    def delete_days(set_list):
        for i in set_list:
            DeleteGenerator.delete_day(i)

    @staticmethod
    def generate_set_list(list_list):
        set_list = []
        result = []
        for i in list_list:
            if i.find("...") != -1:
                first_day, last_day = i.split("...")
                year1, month1, day1 = first_day.split("-")
                year2, month2, day2 = last_day.split("-")
                for y in range(int(year1), int(year2) + 1):
                    for m in range(DeleteGenerator.months_start(y, int(year1), int(month1)),
                                   DeleteGenerator.months_end(y, int(year1), int(year2), int(month2))):
                        for d in range(DeleteGenerator.days_start(y, m, int(month1), int(day1)),
                                       DeleteGenerator.days_end(y, m, int(year2), int(month2), int(day2))):
                            result.append("{0:0=2d}".format(y) + "-" + "{0:0=2d}".format(m) + "-" + "{0:0=2d}".format(d))

            else:
                result.append(i)
            set_list = set_list + result

        return set_list

    @staticmethod
    def generate_list(availability_msg_queue):
        list_list = []
        for i in availability_msg_queue:
            list_list = list_list + i.get_payload()["slot"]
        return list_list

    @staticmethod
    def days_start(y, m, month1, day1):
        if month1 == m:
            return day1
        else:
            return 1

    @staticmethod
    def days_end(y, m, year2, month2, day2):
        if month2 == m and year2 == y:
            return day2 + 1
        else:
            return monthrange(y, m)[1] + 1

    @staticmethod
    def months_start(y, year1, month1):
        if year1 == y:
            return month1
        else:
            return 1

    @staticmethod
    def months_end(y, year1, year2, month2):
        if year1 == y:
            if year2 > year1:
                return 13
            else:
                return month2 + 1
        else:
            return month2 + 1


    @staticmethod
    def repertoire(path):
        dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path+directory)]
        x=dir_list[0]
        for i in dir_list:
            if(x>i):
                x=i
        
        return x
    
            
    def __init__(self):
    
        print (time.strftime("%H:%M:%S"))
        print (time.strftime("%d/%m/%Y"))
        
        i = datetime.datetime.now() - datetime.timedelta(days=1)
         
        print (i.year)
        print (i.month)
        print (i.day)
        
        if(i.month<10):
            monthstr="0"+str(i.month)
        else:
            monthstr=str(i.month)
        
        if(i.day<10):
            daystr="0"+str(i.day)
        else:
            daystr=str(i.day)
                    
        dd =str(i.year)+"-"+monthstr+"-"+daystr
        print(dd)
    
        yeardd, monthdd, daydd = dd.split("-")
       
        yeardd = int(yeardd)
        monthdd = int(monthdd)
        
        
        path = '/reservation/'
        # list of all content in a directory, filtered so only directories are returned
        datedebut=""
        
        #year
        yearpath=DeleteGenerator.repertoire(path)
       
        yeardb = int(yearpath)
        
        if(yeardb < yeardd):
            while(yeardb!=yeardd):
                print("delete year", yeardb)
                DeleteGenerator.delete_year(yeardb)
                yeardb+=1
        print("yeyyyyy",yeardb)
                
        datedebut+=str(yeardb)+"-"
        path+=str(yeardb)+"/"
        
        #month
        
        monthpath=DeleteGenerator.repertoire(path)
        
        monthdb = int(monthpath)
       
                
        if(monthdb < monthdd):
            while(monthdb != monthdd):
                if(monthdb<10):
                    monthstr ="0"+str(monthdb)
                else:
                    monthstr=str(monthdb)
                print("delete month", monthdb)
                DeleteGenerator.delete_month(monthstr,yeardd)
                monthdb+=1
        print("moooooommm",monthstr)
        
        if(monthdb<10):
            monthstr ="0"+str(monthdb)
        else:
            monthstr=str(monthdb)
        datedebut+=monthstr+"-"
        path+=monthstr+"/"  
         
         #day
        daypath=DeleteGenerator.repertoire(path)
        datedebut+=daypath
        path+=daypath+"/"
        print("path:",path)
        print("datedebut:",datedebut)
      
         
        c1 = Capsule()
        c1.set_payload({"slot": [datedebut+"..."+dd]})
        #c2 = Capsule()
        #c2.set_payload({"slot": ["2017-02-17...2017-02-20", "2017-02-21"]})
        #print(DeleteGenerator.generate_set_list(DeleteGenerator.generate_list([c1])))
        
        DeleteGenerator.delete_days(DeleteGenerator.generate_set_list(DeleteGenerator.generate_list([c1])))
    
        
                
        
        
