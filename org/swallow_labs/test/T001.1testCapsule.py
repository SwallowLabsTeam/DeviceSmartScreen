from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleStatus import CapsuleStatus
from org.swallow_labs.tool.CapsuleType import CapsuleType


capsule = Capsule(20)
capsule.set_id_receiver(10)
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule.set_status_capsule(CapsuleStatus.NO)
capsule.set_payload("payload")
capsule.set_type(CapsuleType.PAYLOAD)
print("capsule id: {}".format(capsule.get_id_capsule()))
print("capsule id_reciver: {}".format(capsule.get_id_receiver()))
print("capsule id_sender: {}".format(capsule.get_id_sender()))
print("capsule status: {}".format(capsule.get_status_capsule()))
print("capsule type: {}".format(capsule.get_type()))
print("capsule payload: {}".format(capsule.get_payload()))