# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager, (including Django) as well as custom modules

# import as module
import datetime

today = datetime.date.today()

# print(today)

# import specific module inside the module
from datetime import date
print(f'date: {date.today()}') 

# time
from time import time
print(f'time: {time()}')

# PIP package manager for python

from camelcase import CamelCase 

c = CamelCase()

# print(c.hump('selam alEykum!')) # camel case the first word

# Custom module validator.py

from validator import validate_email

email = 'testmail.com'

if(validate_email(email)):
    print('Valid email')
else:
    print(f'{email} is not a valid email')
