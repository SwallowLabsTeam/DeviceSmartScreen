from org.swallow_labs.model.EmergencyToolBox import *

b = Broker(5001,6001)
capsule = Capsule("4")
capsule.set_type("PAYLOAD")
capsule.set_payload(json.dumps({'nom': 'gammoudi', 'prenom': 'seif'}))
capsule.set_id_receiver("0")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule2 = Capsule("6")
capsule2.set_type("PAYLOAD")
capsule2.set_payload(json.dumps({'nom': 'Sallemi', 'prenom': 'Akram'}))
capsule2.set_id_receiver("20")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
b.message_list=[capsule,capsule2]

p=EmergencyToolBox()
b.backend.close()
b.frontend.close()
p.snapshot(b)
print('Snapshot DONE')
