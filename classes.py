# A class is like a blueprint for creating objects. An object has properties and methods(functions)  associated with it. Almost everything in Py is an object

# Create Class

class User:
    # constructor
    def __init__(self,name, age, email):
        self.name =name
        self.age = age
        self.email = email

# Init USer object

koli = User('Sokol Paja',122,'asd@asd')
koli1 = User('Sokol Paja1',1221,'asd@a1sd')

# print(koli.__dict__)
# print(koli1.__dict__)

# Extend class

class Customer(User):
     # constructor
    def __init__(self,name, age, email):
        self.name =name
        self.age = age
        self.email = email
        self.balance = 0
    
    def set_balance(self,balance):
        self.balance = balance
        
# init customer

customer = Customer('asd asd', 121,'asd@asd.asd')
customer.set_balance(1256)
print(customer.__dict__)
