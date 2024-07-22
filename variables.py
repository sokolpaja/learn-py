# '#' symbol is for comments in python

# A 'variable' is a container of  a value, which can be of various type

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''
"""
same us up
multiline comment
Variables Roles:
    - Variables names are case sensitive (name and NAME are different variables)
    - Must start with a letter or an _(underscore)
    - Can have numbers but can not start with a number
"""

x = 19          #integer
y = 11.4        # float
name = 'Sokol'  # string
is_cool = True  # boolean  

# we can do multiple assignment
a,b,surname,is_good = (1,9.5,'Paja', False)

print('Selam!',x,y,name,is_cool)

# Basic math
a = x+y
print('Basic math a = x+y = ',a)
print('we can print type of a variable: type(x):',type(x))
print('-------')

# we can change a variable typically from string to other vars
# Casting
x = str(x)
print('type of x is changed from int to str:', type(x))
print('-------')

# other Casting

y = int(y)
print('y:float casted as int: ', type(y),y)
print('-------')

z=float(y)
print('z: int converted to float number',type(z),z)