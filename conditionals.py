#  If/Else conditions are used to decide to do something based on something being true or false
x=10
y=20
z=20

# Comparison Operators (==,!=,>,<, >=, <=) -  used to compare values
# Simple if
# if x> 0:
#     print(f'{x} is greater than 0')
    
# if x > 2 and y <= 30:
#     print(f'{x} greater than 2 and {y} less or equal than 30')
# Logical Operators (and, or, not) - used to combine conditional statements 
# if x > 2 or x <= 30:
#     print(f'{x} greater than 2 or less or equal than 30')

# nested conditionals

# if x> 10:
#     print(f'{x} greater than 10')
# elif y > 20:
#     print('x not greater than 10 and y greater than 20')
# else:
#     print(f'{x} not greater than 10, and {y} not greater than 20 ')

# Membership Operators (np, not in) - Membership operators are used to test if a sequence is presented in an object (dict) 

numbers = [1,2,10,111]

# in
if x in numbers:
    print(f'{x} is in {numbers}')

# not in
if y not in numbers:
    print(f'{y} is not in {numbers}')