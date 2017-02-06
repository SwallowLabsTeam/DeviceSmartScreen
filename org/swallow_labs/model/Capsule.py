from org.swallow_labs.model.Parser import Parser
import json
import time
from org.swallow_labs.log.LoggerAdapter import LoggerAdapter

class Capsule:


    """
        Class creating a capsule object:

        G{classtree}

        DESCRIPTION
        ===========
        Create a capsule

        RETURN
        ======
        Return a capsule

        @param id_sender:    Sender ID
        @param j:    Json object

        @type id_sender: int
        @type j: String

        @ivar self.id_sender:    Sender ID
        @ivar self.id_receiver:    Receiver ID
        @ivar self.priority:    Capsule priority
        @ivar self.payload:    Message wanted to send
        @ivar self.type:    Message type (PAYLOAD, READY, END)
        @ivar self.sending_date:    Capsule sending date
        @ivar self.receiving_date:    Capsule receiving date
        @ivar self.status_capsule:    Capsule status(YES if read it and NO if still not read it by the broker)
        @ivar self.tts      Capsule time taking to send
        @ivar self.ACK      Capsule ACK(YES/NO if YES it an ACK or is simple message)
        """

    cpt_capsule = 0

    my_logger = LoggerAdapter(Parser().get_capsule_log_param())

    def __init__(self, id_sender=None, type=None, j=None):
        """
            :

        """

        if j is None:
            self.id_capsule = str(Capsule.capsule_id()).zfill(10)
            self.id_sender = id_sender
            # By default the status of the capsule is not yet read by the broker
            self.status_capsule = "NO"
            self.type = type
            # add to the capsule, date of sending
            self.sending_date = time.ctime()
            Capsule.my_logger.log_init_capsule(self.id_capsule, self.get_id_sender(), self.get_type())
            self.ACK= "NO"
        else:
            self.__dict__ = json.loads(j)


    @staticmethod
    def capsule_id():

        if Capsule.cpt_capsule == 9999999999:
            return 1

        Capsule.cpt_capsule += 1
        return Capsule.cpt_capsule
    # Capsule getters

    def get_id_capsule(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule ID

        """
        return self.id_capsule

    def get_tts(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule tts

        """
        return self.tts

    def get_ACK(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule ACK

        """
        return self.ACK
    def get_id_sender(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the sender ID

        """
        return self.id_sender

    def get_id_receiver(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the receiver ID

        """
        return self.id_receiver

    def get_priority(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule priority

        """
        return self.priority

    def get_sort(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule sort

        """
        return self.sort
    def get_payload(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the payload

        """
        return self.payload

    def get_status_capsule(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule status

        """
        return self.status_capsule

    def get_type(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule type

        """
        return self.type

    def get_sending_date(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the time of sending of the capsule

        """
        return self.sending_date

    def get_receiving_date(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the time of receiving of the capsule

        """
        return self.receiving_date

    # Capsule setters

    def set_id_receiver(self, id_receiver):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the receiver ID

        """
        self.id_receiver = id_receiver

    def set_priority(self, priority):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the capsule priority

        """
        self.priority = priority

    def set_payload(self, payload):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the payload

        """
        self.payload = payload

    def set_sending_date(self, sending_date):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the sending date

        """
        self.sending_date = sending_date

    def set_yes_ACK(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to st yes to the capsule ACK

        """
        self.ACK ="YES"

    def set_tts(self,tts):
        """

        DESCRIPTION
        ===========
        Method providing a way to st the capsule tts

        """
        self.tts = tts

    def set_receiving_date(self, receiving_date):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the receiving date

        """
        self.receiving_date = receiving_date

    def set_status_capsule(self, status_capsule):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the capsule status

        """
        self.status_capsule = status_capsule

    def set_type(self, type):
        """

        DESCRIPTION
        ===========
        Method Setting capsule type

        """
        self.type = type

    def set_sort(self, sort):
        """

        DESCRIPTION
        ===========
        Method Setting capsule sort

        """
        self.sort = sort

    def print_capsule(self):
        """

        DESCRIPTION
        ===========
        Method Print Capsule

        """
        return('Capsule ID: {}, Priority : {}, ID sender : {}, ID receiver : {}, Capsule Status : {},'
              ' Capsule type : {}, Payload : {}, Sending date : {}, Capsule Sort : {}, Capsule ACK : {}'.format(self.get_id_capsule(),
                                                                                                self.get_priority(),
                                                                                                self.get_id_sender(),
                                                                                                self.get_id_receiver(),
                                                                                                self.get_status_capsule(),
                                                                                                self.get_type(),
                                                                                                self.get_payload(),
                                                                                                self.get_sending_date(),
                                                                                                self.get_sort(),
                                                                                                self.get_ACK()
                                                                                                ))
