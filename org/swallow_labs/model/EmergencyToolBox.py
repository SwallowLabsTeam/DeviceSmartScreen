from org.swallow_labs.model.Broker import*
import socket
from org.swallow_labs.model.Capsule import *
from org.swallow_labs.tool.CapsulePriority import *
import hashlib


class EmergencyToolBox:
    """
        Class creating a EmergencyToolBox object:

        G{classtree}

        DESCRIPTION
        ===========
        Create a EmergencyToolBox

        RETURN
        ======
        Return a EmergencyToolBox

        @ivar self.file_store    : a path to create snapshot file


    """
    def __init__(self):
        """


        """
        # Parse the config file and get the path
        self.file_store = Parser().get_snapshot_param()

    def store(self, element_list, obj):
        """
            DESCRIPTION
            ===========
            Method store broker info and broker message list in a json file
            @param element_list: the list to store in the json file
            @param obj: the broker to store info in the json file
            @type element_list: list
            @type obj : Broker
        """
        # Define date and broker info and put them in dict
        date = time.ctime()
        adr = socket.gethostbyname(socket.gethostname())
        backend = str(obj.id_backend)
        frontend = str(obj.id_frontend)
        md5_data = str(str(date)+str(adr)+backend+frontend)
        a = {'date': date, 'broker_info': {"adr":adr , "backend": backend, "frontend": frontend}}
        # Put message list in the dict
        a['msg_list']=[]
        for x in element_list:
            a['msg_list'].append(json.dumps(x.__dict__))
        # Prepare data to MD5 hash
        for y in a['msg_list']:
            md5_data=md5_data+str(y)
        # Get data MD5 digest and put it in the dict
        md5_hash = hashlib.md5(str(md5_data).encode("utf-8")).hexdigest()
        a["md5_hash"]=md5_hash
        # Dump the dict in the snapshot file
        with open(self.file_store+'/'+str(time.strftime("%Y%m%d"))+'_'+str(adr)+':'+backend+'**'+frontend+'.snp', "w") as json_file:
            json.dump(a, json_file)

    def snapshot(self, obj):
        """
            DESCRIPTION
            ===========
            Method do the snapshot
            @param obj: the broker to do snapshot
            @type obj : Broker
        """
        element_list = obj.snapshot()
        self.store(element_list, obj)

    @staticmethod
    def reload(path):
        """
            DESCRIPTION
            ===========
            Method store broker info and broker message list in a json file
            @param path: the path of the file to get broker param to reload a broker instance
            @type path: str
        """
        # Open the file and load data
        son_data = open(path).read()
        data = json.loads(son_data)
        data_check = str(str(data["date"])+str(data['broker_info']["adr"])+str(data['broker_info']['backend'])+str(data['broker_info']['frontend']))
        for y in data["msg_list"]:
            data_check += str(y)
        data_hash = hashlib.md5(str(data_check).encode("utf-8")).hexdigest()
        # Check data digest
        if str(data_hash) == data["md5_hash"]:
            #Reload broker instance with data from snapshot file
            li = []
            for x in data["msg_list"]:
                y = json.loads(x)
                c = Capsule()
                c.set_id_receiver(y["id_receiver"])
                c.id_capsule = y["id_capsule"]
                c.set_payload(y["payload"])
                c.id_sender = y["id_sender"]
                c.set_priority(y["priority"])
                c.set_sending_date(y['sending_date'])
                c.set_status_capsule(y['status_capsule'])
                c.set_type(y['type'])
                li.append(c)

            b = Broker(data['broker_info']['frontend'], data['broker_info']['backend'])
            b.message_list = li
            print("Correct MD5 check")
            return b
        else:
            # data is changed no reload
            print("FATAL ERROR THE DATA IS CHANGED")
            return None













