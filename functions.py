# A function is a block of code which oly runs when its called. In Py, we do not use curly brackets, we use indentation with tabs or spaces

# Create a function

def init(name):
    print(f'Selam aleykum {name}')

init('Sokol')

# lambda functions like arrow functions
# can take any number of args but can only have 1 expression

getSum = lambda num1,num2 : num1 + num2

print(getSum(1,2))