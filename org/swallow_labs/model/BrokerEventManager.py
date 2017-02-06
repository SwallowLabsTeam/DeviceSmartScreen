import zmq
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.model.Parser import Parser
from  org.swallow_labs.model.Client import *
from org.swallow_labs.model.SendProcessor import *
import json

class BrokerEventManager:


    """
        Class creating a broker object

        G{classtree}

        DESCRIPTION
        ===========
        Create a broker

        RETURN
        ======
        Return a broker

        @param id_frontend:    port number for the front-end socket
        @ivar self.frontend:    front-end socket
        @ivar self.poller:    A stateful poll object

        @type id_frontend: int


    """

    def __init__(self, id_frontend):
        """


        """
        self.id_frontend = id_frontend
        # Prepare context and sockets
        # Create a Context object to be able to call socket method
        context = zmq.Context()
        self.frontend = context.socket(zmq.ROUTER)
        # Create a ROUTER socket for front-end connections
        self.frontend.bind("tcp://*:" + str(self.id_frontend))
        # bind front-end socket
        #self.client = Client(self.id_client,Parser.get_backend_broker_list())
        #self.client.generate()
        # create a client to connect to the MOM broker
        self.poller = zmq.Poller()
        # Create a Poller object to detect the active sockets at a given time
        self.poller.register(self.frontend, zmq.POLLIN)
        # Register the front-end sockets into the poller

    def start(self,client):
        """

        DESCRIPTION
        ===========
        Method describing the behaviour of the broker it is the main loop in which he receives messages
        and forwards them to the MOM
        """
        while(True): 
            print("ok")
            f = open("/home/test.txt", 'w')
    
               
            f.write("salmen  okiiii")
            # write in the file the capsule payload that contains information about the new ldap entry
            f.close()
            socks = dict(self.poller.poll())
            # Convert the return of the poll method into a dictionary
            if socks.get(self.frontend) == zmq.POLLIN:
                # if the the argument iss true, it means that a message is received on the front-end socket
                b_client_id, b_capsule = self.frontend.recv_multipart()
                print(b_client_id, b_capsule)
                # receive client id and capsule as bytes
                #client_id = b_client_id.decode('utf8')
                c_recv = Capsule(j=json.loads(b_capsule.decode('utf8')))
                #convert capsule to str
                
                #load data in a capsule object
                print(client.id_client)
                s= SendProcessor(c_recv)
                s.send_capsule(client)
                #send capsule to the mom broker using mom client

