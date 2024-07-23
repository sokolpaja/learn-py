# JSON is commonly used with data APIS. How can we can parse JSON into py dictionary

import json

#  Sample JSON

userJSON = '{"name":"asd","last_name":"asd"}'

# Parse to dict
user  = json.loads(userJSON)

print(user['name'])

# convert dict to json

car = {'make':'camel', 'model':'Fast'}

carJSON = json.dumps(car)

print(carJSON)