class CapsuleACK:


    """
        Class creating a capsuleACK object:

        G{classtree}

        DESCRIPTION
        ===========
        Create a capsule object to know aquitment sended

        RETURN
        ======
        Return a capsuleACK

        @param id_capsule:    capsule ID
        @param status:        status "YES"/"NO"

        @type id_capsule: int
        @type status: String

        """

    def __init__(self,id_capsule,status):
        """

        """
        self.id_capsule = id_capsule
        self.status = status

    def get_id_capsule(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsuleACK ID

        """
        return self.id_capsule

    def get_status(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsuleACK ID

        """
        return self.status

    def set_id_capsule(self, id_capsule):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the receiver ID

        """
        self.id_capsule = id_capsule

    def set_status(self, status):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the receiver ID

        """
        self.status = status


