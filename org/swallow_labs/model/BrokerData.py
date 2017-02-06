class BrokerData:
    """
        Class creating a BrokerData object
        G{classtree}
        DESCRIPTION
        ===========
        Class containing the necessary data about the brokers to be able to initialize the clients

        @param address:    The Broker's ip address
        @param port:    port number

        @type address: string
        @type port: int
    """
    def __init__(self, address, port):
        self.address = address
        self.port = port

