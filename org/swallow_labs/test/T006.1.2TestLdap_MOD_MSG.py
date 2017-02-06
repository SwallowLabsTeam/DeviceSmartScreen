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

capsule.set_payload({'att':['dn','changetype','replace'],
                     'dn': 'ECode=31,o=Establishments,o=WebApp,dc=swallow,dc=tn',
                     'changetype': 'modify',
                     'replace':  ['Eadress','Ebalance','ECode','EEmail','Efax','Ename','Ephone','ESector','EShortName','EuserAccountNum'],
                     'Eadress': 'route el ain',
                     'Ebalance': '11111',
                     'ECode': '31',
                     'EEmail': 'xxxxx@xxxx.com',
                     'Efax': '78888885',
                     'Ename': 'tt',
                     'Ephone': '745487894',
                     'ESector': 'telecom',
                     'EShortName': 'ttt',
                     'EuserAccountNum': '777'

                     })


capsule.set_id_receiver("55")
#capsule.set_id_recNOeiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule.set_sort(CapsuleSort.LDAP_MOD_MSG)



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
