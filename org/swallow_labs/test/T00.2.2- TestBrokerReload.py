from org.swallow_labs.model.EmergencyToolBox import *
p=EmergencyToolBox()
k=p.reload("/home/salmen/20160617_127.0.1.1:6001**5001.snp")
print("Reload Broker DONE with:")
print("id_backend: "+k.id_backend)
print("id_frontend: "+k.id_frontend)
print("Message liste:")
for x in k.message_list:
    print(x.print_capsule())
