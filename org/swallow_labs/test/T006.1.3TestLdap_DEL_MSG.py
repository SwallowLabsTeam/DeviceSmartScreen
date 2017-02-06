from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType
from org.swallow_labs.tool.CapsuleSort import *
import time

l = Parser.get_backend_broker_list()
c = Client(77, l)
c.generate()
print("client launched")
capsule = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule.set_type("PAYLOAD")
capsule.set_payload({
                     'dn': 'ECode=30,o=Establishments,o=WebApp,dc=swallow,dc=tn'

                     })



capsule.set_id_receiver("55")
#capsule.set_id_recNOeiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule.set_sort(CapsuleSort.LDAP_DEL_MSG)



if c.push(capsule) == 1:
    print("capsule sended")
    print(capsule.id_sender)
time.sleep(5)
print(c.id_client)
if c.pull():
    if len(c.pull_list) == 0:
        print("No Messaages")
    else:
        for x in c.pull_list:
            print("Capsule received")
            print(x.print_capsule())
            print(x.get_sort())