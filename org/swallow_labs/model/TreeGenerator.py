import json
import os
from calendar import monthrange



class TreeGenerator:
    
    
    def __init__(self):
        pass
        

    
   
    def create_day(self,date,time):
        print(date)
        year, month, day = date.split("-")
        with open('../conf/Configuration_Display.json') as json_config:
            config = json.load(json_config)
            json_config.close()
        with open(config["standard_json_file"]) as json_data:
            d = json.load(json_data)
            json_data.close()
        d["planning"]["annee"] = str(year)
        d["planning"]["mois"] = str(month)
        d["planning"]["jour"] = str(day)
        d["planning"]["segment_duration_min"] = str(time)
        if not os.path.exists(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day)):
            os.makedirs(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day))
        else:
            print("dellleeeeteee")
            shutil.rmtree(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day))
            os.makedirs(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day))
            
        with open(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day) + "/Planning.json", "w") as output:
            os.utime(config['reservation_root_directory'] + "/" + str(year) + "/" + str(month) + "/" + str(day) + "/Planning.json", None)
            json.dump(d, output)
            output.close()
        for j in range(0, 24):
            for i in range(0, 60, int(time)):
                if not os.path.exists(config['reservation_root_directory'] + "/" + year + "/" + month + "/" + day + "/" + "{0:0=2d}".format(j) + "/" + "{0:0=2d}".format(i)):
                    os.makedirs(config['reservation_root_directory'] + "/" + year + "/" + month + "/" + day + "/" + "{0:0=2d}".format(j) + "/" + "{0:0=2d}".format(i))
                pass

    
    def create_days(self,set_list,time):
        for i in set_list:
            self.create_day(i,time)

    
    def generate_set_list(self,list_list):
        set_list = []
        result = []
        for i in list_list:
            if i.find("...") != -1:
                first_day, last_day = i.split("...")
                year1, month1, day1 = first_day.split("-")
                year2, month2, day2 = last_day.split("-")
                for y in range(int(year1), int(year2) + 1):
                    for m in range(self.months_start(y, int(year1), int(month1)),
                                   self.months_end(y, int(year1), int(year2), int(month2))):
                        for d in range(self.days_start(y, m, int(month1), int(day1)),
                                       self.days_end(y, m, int(year2), int(month2), int(day2))):
                            result.append("{0:0=2d}".format(y) + "-" + "{0:0=2d}".format(m) + "-" + "{0:0=2d}".format(d))

            else:
                result.append(i)
            set_list = set_list + result

        return set_list

    
    def generate_list(self,availability_msg_queue):
        list_list = []
        for i in availability_msg_queue:
            list_list = list_list + i.get_payload()["slot"]
        return list_list

    
    def days_start(self,y, m, month1, day1):
        if month1 == m:
            return day1
        else:
            return 1

    
    def days_end(self,y, m, year2, month2, day2):
        if month2 == m and year2 == y:
            return day2 + 1
        else:
            return monthrange(y, m)[1] + 1

    
    def months_start(self,y, year1, month1):
        if year1 == y:
            return month1
        else:
            return 1

    
    def months_end(self,y, year1, year2, month2):
        if year1 == y:
            if year2 > year1:
                return 13
            else:
                return month2 + 1
        else:
            return month2 + 1
    
    def planing_file(self,time):
        
        lst_planing = []

        x=60/int(time)

        tt=0
        creneau='[]'
        cc=""
        dataphoto = {}
        dataphoto['id'] = ''
        datavideo = {}
        datavideo['id'] = ''
       
        
        datacrenau = {}
        datacrenau['id'] = 'value'
        datacrenau['holder'] = 'swallow'
        datacrenau['video'] = datavideo
        datacrenau['photo'] = dataphoto

        for i in range(int(x)):
            if(tt<10):
                t1="0"+str(tt)
            else:
                t1=str(tt)
            datacrenau = {}
            datacrenau['id'] = t1
            datacrenau['holder'] = 'swallow'
            datacrenau['video'] = datavideo
            datacrenau['photo'] = dataphoto
            
            #c= '{"id": "'+t1+'","holder": "swallow","video": { "id": "" },"photo": { "id": "" }}'
            
            #lst_planing.append("{'id': '"+t1+"','holder': 'swallow','video': { 'id': '' },'photo': { 'id': '' }}")
            lst_planing.append(datacrenau)
            tt+=int(time)
        print("1111111111111111111")
        with open('../conf/Planning_file.json') as json_dataPlaning:
            data = json.load(json_dataPlaning)
            json_dataPlaning.close()
        
        print("goooooooooooooood")
           
        for i in range(24):
            data["planning"]["heure"][i]["creneau"]=lst_planing
       
        print("modiiiiit:",data)
        with open('../conf/Planning.json', 'w') as fichier:
            json.dump(data, fichier, sort_keys=True, indent=4,
                      ensure_ascii=False)

