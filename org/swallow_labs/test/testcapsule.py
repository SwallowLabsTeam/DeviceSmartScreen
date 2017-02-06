'''Script to instance a client stub and push two capsule'''
from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
import zmq
import socket
import json

capsule = Capsule(20, CapsuleType.PAYLOAD)
capsule.set_type("PAYLOAD")
capsule.set_payload({'id': 17})
capsule.set_id_receiver("75")
capsule.set_sort("ds")
capsule.ACK="YES"
capsule.set_tts(10)
#capsule.set_id_receiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)

context = zmq.Context(1)

        # Create a DEALER socket
socket = context.socket(zmq.DEALER)
socket.setsockopt(zmq.IDENTITY, b'A')
socket.connect("tcp://127.0.0.1:7000")

socket.send_json(json.dumps(capsule.__dict__))



