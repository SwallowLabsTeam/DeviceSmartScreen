from org.swallow_labs.model.Parser import *

class LdapParam:
    """
        Class creating a LdapParam object
        G{classtree}
        DESCRIPTION
        ===========
        Class containing the necessary data about the ldap connexion param

    """

    def __init__(self):
        self.admin = Parser.get_ldap_param()[0]
        self.password = Parser.get_ldap_param()[1]


