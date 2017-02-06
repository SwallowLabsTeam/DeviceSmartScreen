from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType
from org.swallow_labs.tool.CapsuleSort import *

import time
from org.swallow_labs.model.SendProcessor import *
import org.swallow_labs.model.SendProcessor
l = Parser.get_backend_broker_list()
c = Client(77, l)
c.generate()
print("client launched")
capsule = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule.set_type("PAYLOAD")

capsule.set_payload({'att': ['dn', 'objectClass', 'AFirstName', 'ALastName', 'AAdress', 'userPassword', 'AEmail',
                             'APhone', 'ADateOfBirth', 'APicture', 'ACIN', 'AAssigningContent', 'ContractAdd',
                             'ContractUpdate', 'ContractDelete', 'ContractDisplay', 'ContractPrint', 'ContractSign',
                             'ContractValidator', 'ContractAuth', 'AccountAdd', 'AccountUpdate', 'AccountDelete',
                             'AccountDisplay', 'AccountPrint', 'AccountValidator', 'AccountAuth', 'InvoiceAdd',
                             'InvoiceUpdate', 'InvoiceDelete', 'InvoiceDisplay', 'InvoicePrint', 'InvoiceSign',
                             'InvoiceAuth', 'InvoiceValidator', 'ClientAdd', 'ClientUpdate', 'ClientDelete',
                             'ClientDisplay', 'ClientPrint', 'ClientAccountManagment', 'ClientValidator', 'ClientAuth',
                             'ScreenActivation', 'ScreenDelete', 'ScreenDisplay', 'ScreenPrint', 'ScreenGA',
                             'ScreenONOFF', 'ScreenClear', 'ScreenMonitoring', 'ScreenValidator', 'ScreenAuth',
                             'ScreenUpdate', 'ScreenShow', 'ScreenUpdateSystem', 'SegmentAffect', 'SegmentUpdate',
                             'SegmentDelete', 'SegmentPrint', 'SegmentDisplay', 'SegmentValidator', 'SegmentAuth',
                             'TariffAdd', 'TariffUpdate', 'TariffDelete', 'TariffPrint', 'TariffAffect',
                             'TariffValidator', 'TariffAuth', 'BookingAdd', 'BookingUpdate', 'BookingDelete',
                             'BookingDisplay', 'BookingPrint', 'BookingValidator', 'BookingAuth', 'ContentAdd',
                             'ContentDelete', 'ContentDisplay', 'ContentValidator', 'ContentAuth', 'RoleAdd',
                             'RoleDelete', 'RoleUpdate', 'RoleDisplay', 'RolePrint', 'RoleValidator', 'RoleAuth',
                             'ArticleAdd', 'ArticleUpdate', 'ArticleDelete', 'ArticleDisplay', 'ArticlePrint',
                             'ArticleAffect', 'ArticleValidator', 'ArticleAuth', 'SignatureAdd', 'SignatureValidator',
                             'SignatureAuth', 'FirmwareAdd', 'FirmwareUpdate', 'FirmwareDelete', 'FirmwareDisplay',
                             'FirmwarePrint'],

                     'dn': 'AEmail=xxx@aaatn,o=Administrators,o=WebApp,dc=swallow,dc=tn',
                     'objectClass': ['top', 'AppAdministrator', 'ContractManagment', 'AccountManagment',
                                     'InvoiceManagment', 'ClientManagment', 'ScreenManagment', 'SegmentManagment',
                                     'TariffManagment', 'BookingManagment', 'ContentManagment', 'RoleManagment',
                                     'ArticleManagment', 'SignatureManagment', 'FirmwareManagment'],

                     'AFirstName': 'route el sokra',
                     'ALastName': '444',
                     'AAdress': 'fsdfsd',
                     'userPassword': 'dsfs',
                     'AEmail': 'xxx@aaatn',
                     'APhone': 'dsfsd',
                     'ADateOfBirth': 'sdfdsf',
                     'APicture': 'dsffds',
                     'ACIN': 'fdsfsd',
                     'AAssigningContent': 'dsfdsf',
                     'ContractAdd': 'dsfds',
                     'ContractUpdate': 'dsfsd',
                     'ContractDelete': 'dsfsdf',
                     'ContractDisplay': 'dsfdsf',
                     'ContractPrint': 'dsffds',
                     'ContractSign': 'dsfdsf',
                     'ContractValidator': 'dsffd',
                     'ContractAuth': 'dsfdsf',
                     'AccountAdd': 'dsfdfs',
                     'AccountUpdate': 'dsfdf',
                     'AccountDelete': 'dsfdsf',
                     'AccountDisplay': 'dfsfds',
                     'AccountPrint': 'dsffds',
                     'AccountValidator': 'dsfdsf',
                     'AccountAuth': 'dsffd',
                     'InvoiceAdd': 'dsfdsf',
                     'InvoiceUpdate': 'dsffsd',
                     'InvoiceDelete': 'dsfdsf',
                     'InvoiceDisplay': 'fsdfsd',
                     'InvoicePrint': 'dfsdsf',
                     'InvoiceSign': 'dsffds',
                     'InvoiceAuth':'ghhfghf',
                     'InvoiceValidator': 'fsdfsd',
                     'ClientAdd': 'dsffds',
                     'ClientUpdate': 'dsffds',
                     'ClientDelete': 'dsfdsf',
                     'ClientDisplay': 'dsfdsf',
                     'ClientPrint': 'dsfdfs',
                     'ClientAccountManagment': 'dsfdsf',
                     'ClientValidator': 'dsfdsf',
                     'ClientAuth': 'dsfdfs',
                     'ScreenActivation': 'fdsfsd',
                     'ScreenDelete': 'dsfdsf',
                     'ScreenDisplay': 'dsfdsf',
                     'ScreenPrint': 'dsfdfs',
                     'ScreenGA': 'dsfdsf',
                     'ScreenONOFF': 'dsfdsf',
                     'ScreenClear': 'dsfdfs',
                     'ScreenMonitoring': 'dsfdsf',
                     'ScreenValidator': 'dsfdsf',
                     'ScreenAuth': 'dsfdsf',
                     'ScreenUpdate': 'dsfdsf',
                     'ScreenShow': 'dsffsd',
                     'ScreenUpdateSystem': 'dfsdsf',
                     'SegmentAffect': 'dsffsd',
                     'SegmentUpdate': 'sdfdsf',
                     'SegmentDelete': 'dsfdsf',
                     'SegmentPrint': 'dsffsd',
                     'SegmentDisplay': 'dsfdsf',
                     'SegmentValidator': 'dsfdfs',
                     'SegmentAuth': 'dsfdsf',
                     'TariffAdd': 'dsfsd',
                     'TariffUpdate': 'dsfdsf',
                     'TariffDelete': 'dsfdsf',
                     'TariffPrint': 'dsfdsf',
                     'TariffAffect': 'dsffd',
                     'TariffValidator': 'dsfsd',
                     'TariffAuth': 'dsfsdf',
                     'BookingAdd': 'dsf',
                     'BookingUpdate': 'dfsdsf',
                     'BookingDelete': 'fsdfsd',
                     'BookingDisplay': 'dsffds',
                     'BookingPrint': 'dsfdsf',
                     'BookingValidator': 'dsfdsf',
                     'BookingAuth': 'dsffsdsd',
                     'ContentAdd': 'dsffsdfsd',
                     'ContentDelete': 'dsfsd',
                     'ContentDisplay': 'dsffsd',
                     'ContentValidator': 'dsffsd',
                     'ContentAuth': 'dsfdsffsd',
                     'RoleAdd': 'dsfsdfdfs',
                     'RoleDelete': 'sdffsd',
                     'RoleUpdate': 'dsfsdf',
                     'RoleDisplay': 'dsfdsf',
                     'RolePrint': 'sdffsd',
                     'RoleValidator': 'dsfdfs',
                     'RoleAuth': 'dsfdsf',
                     'ArticleAdd': 'dsffsd',
                     'ArticleUpdate': 'dsffsd',
                     'ArticleDelete': 'dsfdsf',
                     'ArticleDisplay': 'fsdfsd',
                     'ArticlePrint': 'dsfdsf',
                     'ArticleAffect': 'dsffsd',
                     'ArticleValidator': 'dsfdfsfsd',
                     'ArticleAuth': 'dsfdsf',
                     'SignatureAdd': 'fsddfs',
                     'SignatureValidator': 'sdfdfs',
                     'SignatureAuth': 'sdfdsf',
                     'FirmwareAdd': 'dsfdsf',
                     'FirmwareUpdate': 'dsfdfs',
                     'FirmwareDelete': 'dsfdsf',
                     'FirmwareDisplay': 'sdfdfs',
                     'FirmwarePrint': 'sdfsdf'})


capsule.set_id_receiver("55")
#capsule.set_id_recNOeiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule.set_sort(CapsuleSort.LDAP_ADD_MSG)

capsule2 = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("55")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
capsule2.set_sort(CapsuleSort.LDAP_ADD_MSG)
s=SendProcessor(capsule)
s.send_capsule(c)
print("send")
for x in org.swallow_labs.model.SendProcessor.sending_list:
    print(x.print_capsule())

time.sleep(5)
'''if c.push(capsule) == 1:
    print("capsule resended")
    print(capsule.id_sender)'''
'''time.sleep(5)
if c.push(capsule) == 1:
    print("capsule resended")
    print(capsule.id_sender)

time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule2 sended")
    print(capsule2.id_sender)
time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule resended")
    print(capsule2.id_sender)

time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule resended")
    print(capsule2.id_sender)'''
#time.sleep(5)
print(c.id_client)
if c.pull():
    if len(c.pull_list) == 0:
        print("No Messaages")
    else:
        for x in c.pull_list:
         print(x.print_capsule())
         print("ACKAAAAAA:", type(x.get_ACK()))

         if (x.get_ACK() == str("YES")):
            pld = x.get_payload()
            print("capsule ack")
            print(pld["id"])
            print("ACKAAAAAA:", x.get_ACK())
            for w in org.swallow_labs.model.SendProcessor.sending_list:
                print("plddddd ",w.get_id_sender())
                if (w.get_id_capsule() == pld["id"]):
                    print("ok")
                    org.swallow_labs.model.SendProcessor.sending_list.remove(w)

for x in org.swallow_labs.model.SendProcessor.sending_list:
    print(x)