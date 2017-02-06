from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import *
import org.swallow_labs.model.RunClient
import org.swallow_labs.model.SocketClient
from subprocess import *
import datetime

class SendProcessor:

    """
        Class creating a SendProcessor object
        G{classtree}
        DESCRIPTION
        ===========
        Class that send capsule to main broker

        @param cpl    : The capsule that will be sent


        @type cpl     : Capsule

    """


    def __init__(self, cpl):
        """
                :

        """
        self.cpl = cpl
        # initialize the capsule  that will be sent
    def send_capsule(self,x):
        SendProcessor.send_in_sending_list(x)
        SendProcessor.append(self.cpl)
        x.push(self.cpl)
        # add capsule to list broker
        print("sending list",org.swallow_labs.model.RunClient.shared_dict['list_item'])
    @staticmethod
    def send_in_sending_list(y):
        for x in org.swallow_labs.model.RunClient.shared_dict['list_item']:
            if SendProcessor.verify_tts(x):
                y.push(x)
                #when is time of tts push capsule


    @staticmethod
    def append(x):
        if x.get_priority() == CapsulePriority.BOOKING_MSG:
            item = org.swallow_labs.model.RunClient.shared_dict['list_item']
            # add list item in item
            item.append(x)
            # add capsule in item list
            org.swallow_labs.model.RunClient.shared_dict['list_item'] = item
            # refresh list item with new list item

    @staticmethod
    def verify_tts(x):
        """

        @param x: Verify tts Capsule
        @return: if the sending time + tts is upper to current time retun True else return false
        @type x: Capsule
        @rtype: bool
        """
        w = datetime.datetime.strptime(x.get_sending_date(), "%a %b %d %H:%M:%S %Y")
        #time send capsule + TTS
        if (w+ datetime.timedelta(0, x.get_tts())>=datetime.datetime.now()):
            return False
        else:
            return True