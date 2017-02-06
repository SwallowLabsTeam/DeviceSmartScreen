" script to instance a client stub and pull messages from brokers"
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

c1 = Client(25, Parser.get_backend_broker_list())
print("Client launched")
c1.generate()
if c1.pull():
    if len(c1.pull_list) == 0:
        print("No Messaages")
    else:
        for x in c1.pull_list:
            print("Capsule received")
            print(x.print_capsule())






