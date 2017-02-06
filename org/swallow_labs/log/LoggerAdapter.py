import logging
import logging.handlers
import json
import socket


class InfoFilter(logging.Filter):

    def filter(self, rec):
        return rec.levelno == logging.INFO


class DebugFilter(logging.Filter):

    def filter(self, rec):
        return rec.levelno == logging.DEBUG


class WarningFilter(logging.Filter):

    def filter(self, rec):
        return rec.levelno == logging.WARNING


class CriticalFilter(logging.Filter):

     def filter(self, rec):
         return rec.levelno == logging.CRITICAL


class ErrorFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR


class LoggerAdapter:

    def __init__(self, arg):

        self.id_logger = str(arg[5])

        self.host = str(arg[0])
        self.port = arg[1]
        self.facility = str(arg[3])
        self.format = arg[4]
        if arg[2] == 'DEBUG':
            self.level = logging.DEBUG
        if arg[2] == 'INFO':
            self.level = logging.INFO
        if arg[2] == 'ERROR':
            self.level = logging.ERROR
        if arg[2] == 'WARNING':
            self.level = logging.WARNING
        if arg[2] == 'CRITICAL':
            self.level = logging.CRITICAL

        self.logger = logging.getLogger(self.id_logger)
        self.logger.setLevel(self.level)
        syslog = logging.handlers.SysLogHandler(address=(self.host, int(self.port)), facility=self.facility)
        #self.logger.addFilter(InfoFilter())
        formatter = logging.Formatter(self.format)
        syslog.setFormatter(formatter)
        self.logger.addHandler(syslog)

    def log(self, msg, level):

        if level is 'debug':
            self.logger.debug(msg)
        elif level is 'info':
            self.logger.info(msg)
        elif level is 'error':
            self.logger.error(msg)
        elif level is 'warning':
            self.logger.warning(msg)
        elif level is 'critical':
            self.logger.critical(msg)

    def log_broker_start(self, arg1, arg2):
        self.logger.info('Broker start: ' + ' with address: ' + str(socket.gethostbyname(socket.gethostname())) + 'PORT: Frontend: ' + str(arg1) + ' Backend: ' + str(arg2))

    def log_broker_send(self, arg1, arg2):
        self.logger.debug('Sent to client {} : {}'.format(arg1, json.dumps(arg2.__dict__)))

    def log_broker_receive(self, arg1):
        self.logger.debug('Received from client {} : {}'.format(arg1.get_id_sender(), json.dumps(arg1.__dict__)))

    def log_client_connect(self, arg1, arg2, arg3):
        self.logger.info('Client {} Connected to {} on port: {}'.format(arg1, arg2, arg3))

    def log_client_push(self, arg1):
        self.logger.debug('Sent : {}'.format(arg1.__dict__))

    def log_client_pull(self, arg1):
        self.logger.debug('Messages received {}'.format(arg1.__dict__))

    def log_server_down(self):
        self.logger.warn('Server down')

    def log_init_capsule(self, arg1, arg2, arg3):
        self.logger.info('Capsule {} created by {} and type {}'.format(arg1, arg2, arg3))

    def log_receive_capsule(self, arg1, arg2, arg3, arg4):
        self.logger.info('Capsule {} received by {} from {} and type {}'.format(arg1, arg2, arg3, arg4))

    def log_missing_file(self, file_name):
        self.logger.error('{} is missing!'.format(file_name))

    def log_treated_capsule(self, arg):
        self.logger.debug('capsule treated {}'.format(arg.__dict__))

    def log_snapshot(self, arg):
        self.logger.info('Broker snapshot done: '+arg)

    def log_sendACK_error_request(self,arg,arg2):
        self.logger.debug('capsule request error id: ' + arg +'  id_client: '+arg2)

    def log_sendACK_error_structure(self,arg,arg2):
        self.logger.debug('capsule structure error id: ' + arg+'  id_client: '+arg2)

    def log_sendACK_error_server_down(self,arg,arg2):
        self.logger.debug('server LDAP down error id: ' + arg+'  id_client: '+arg2)

    def log_sendACK_verif(self, arg, arg2):
        self.logger.debug('capsule is already treated id: ' + arg + '  id_client: ' + arg2)