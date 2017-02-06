"Script to instance a client object and push two capsule and log all"

from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.model.Parser import *
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType

c = Client(5, Parser.get_frontend_broker_list())
print("Client launched")

capsule1 = Capsule(c.id_client, CapsuleType.PAYLOAD)
capsule1.set_payload({'nom': 'gammoudi', 'prenom': 'seif'})
capsule1.set_id_receiver("20")
capsule1.set_priority(CapsulePriority.BOOKING_MSG)

capsule2 = Capsule(c.id_client, CapsuleType.PAYLOAD)
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("20")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
c.generate()

if c.push(capsule1) == 1:
    print("Capsule Sent")

if c.push(capsule2) == 1:
    print("Capsule Sent")

