from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import *
from org.swallow_labs.model.Launcher import *

json_data = open('../conf/Configuration.json').read()
data = json.loads(json_data)
json_data = open('../test/schema').read()
schema = ast.literal_eval(json_data)
try:
    validate(data, schema)  # in case the json data isn't valid this function will throw an exception.
    print("Your json file is VALID")
except ValidationError:
    print("Your json file is INVALID")
client = Client(5, Parser.get_frontend_broker_list())
print("client launched")
broker_launcher = Launcher('../conf/Configuration.json')
