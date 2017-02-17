from org.swallow_labs.log.LoggerAdapter import LoggerAdapter
from Parser import Parser


my_logger1 = LoggerAdapter(Parser().get_device_log_param())
print("tyh", my_logger1)