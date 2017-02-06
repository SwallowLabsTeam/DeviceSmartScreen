import json
from jsonschema import validate, ValidationError
import ast
from org.swallow_labs.model.BrokerData import BrokerData
import socket

class Parser:
    """
        Class creating a Parser object
        G{classtree}
        DESCRIPTION
        ===========
        Class that s handeling the parsing of the json files in order to store data and make it available for use
        by other components

        @param client_path:    path of the json file containing the client infos
        @param broker_path:    path of the json file containing the brokers infos

        @type client_path: string
        @type broker_path: string
    """
    __data = {}
    __backend_broker_list = []
    __frontend_broker_list = []
    __broker_log_param = []
    __client_log_param = []
    __capsule_log_param = []
    __snapshot_param = ''
    __ldap_param = []
    __client_id = ''

    def __init__(self, files_path_list=['../conf/Configuration.json']):
        Parser.read(files_path_list)
        Parser.set_all()

    @staticmethod
    def read(files_path_list, schema_path='../test/schema'):
        schema = ast.literal_eval(open(schema_path).read())
        for f in files_path_list:
            try:
                Parser.__data = {**Parser.__data, **json.loads(open(f).read())}
                if 'Configuration.json' in f:
                    try:
                        validate(json.loads(open(f).read()), schema)
                    except ValidationError:
                        pass
            except FileNotFoundError:
                pass

    @staticmethod
    def set_all():
        Parser.set_backend_broker_list()
        Parser.set_frontend_broker_list()
        Parser.set_broker_log_param()
        Parser.set_capsule_log_param()
        Parser.set_client_log_param()
        Parser.set_snapshot_param()
        Parser.set_ldap_param()
        Parser.set_client_id()
    @staticmethod
    def set_backend_broker_list():
        try:
            for i in range(len(dict(Parser.__data)['net_param']['ip_add'])):
                Parser.__backend_broker_list.append(BrokerData(dict(Parser.__data)['net_param']['ip_add'][i],
                                                               dict(Parser.__data)['net_param']['back_end'][i]))
        except:
            pass

    @staticmethod
    def set_frontend_broker_list():
        try:
            for i in range(len(dict(Parser.__data)['net_param']['ip_add'])):
                Parser.__frontend_broker_list.append(BrokerData(dict(Parser.__data)['net_param']['ip_add'][i],
                                                                dict(Parser.__data)['net_param']['front_end'][i]))
        except:
            pass

    @staticmethod
    def set_broker_log_param():
        try:
            Parser.__broker_log_param = [Parser.__data['log_param']['broker']['host'],
                                         Parser.__data['log_param']['broker']['port'],
                                         Parser.__data['log_param']['broker']['level'],
                                         Parser.__data['log_param']['broker']['facility'],
                                         Parser.__data['log_param']['broker']['format'],
                                         "Broker"]
        except:
            pass

    @staticmethod
    def set_client_log_param():
        try:
            Parser.__client_log_param = [Parser.__data['log_param']['client']['host'],
                                         Parser.__data['log_param']['client']['port'],
                                         Parser.__data['log_param']['client']['level'],
                                         Parser.__data['log_param']['client']['facility'],
                                         Parser.__data['log_param']['client']['format'],
                                         "Client"]
        except:
            pass

    @staticmethod
    def set_capsule_log_param():
        try:
            Parser.__capsule_log_param = [Parser.__data['log_param']['capsule']['host'],
                                          Parser.__data['log_param']['capsule']['port'],
                                          Parser.__data['log_param']['capsule']['level'],
                                          Parser.__data['log_param']['capsule']['facility'],
                                          Parser.__data['log_param']['capsule']['format'],
                                          "Capsule"]
        except:
            pass

    @staticmethod
    def set_snapshot_param():
        try:
            Parser.__snapshot_param = Parser.__data['snapshot_param']['path']
        except:
            pass

    @staticmethod
    def set_ldap_param():
        try:
            Parser.__ldap_param = [Parser.__data['ldap_param']['admin'],
                                   Parser.__data['ldap_param']['password']]
        except:
            pass

    @staticmethod
    def set_client_id():
        try:
            hostname=socket.gethostname()
            Parser.__client_id = Parser.__data['client_id'][hostname]

        except:
            pass

    @staticmethod
    def get_backend_broker_list():
        return Parser.__backend_broker_list

    @staticmethod
    def get_frontend_broker_list():
        return Parser.__frontend_broker_list

    @staticmethod
    def get_broker_log_param():
        return Parser.__broker_log_param

    @staticmethod
    def get_client_log_param():
        return Parser.__client_log_param

    @staticmethod
    def get_capsule_log_param():
        return Parser.__capsule_log_param

    @staticmethod
    def get_snapshot_param():
        return Parser.__snapshot_param

    @staticmethod
    def get_ldap_param():
        return Parser.__ldap_param

    @staticmethod
    def get_client_id():
        return Parser.__client_id

if __name__ == '__main__':

    Parser()


