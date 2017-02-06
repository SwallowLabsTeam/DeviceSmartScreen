"Script to instance a client object and pull messages from all brokers and log all msg"

from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

client = Client(20, Parser.get_backend_broker_list())
print("Client launched")

client.generate()
if client.pull():
    if len(client.pull_list) == 0:
        print("No Messages")
    else:
        for x in client.pull_list:
            print("Capsule received")
