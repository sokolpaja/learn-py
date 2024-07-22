# String in python are surrounded by either single or double quotes marks. Let's look at string formatting and some strings methods

name = 'Sokol'
age = 33

# Concatenating
# print('Selam, my name is ' + name + ' and i am ' + age) # throws error

# print('Selam, my name is ' + name + ' and i am ' + str(age))

# String Formatting
# print(f'Selam, i am {name}, {age}'.format(name=name,age=age))

# String Methods

s = 'selam aleykum!'

# Capitalize a string only the first letter of string, word or sentence.
print(s.capitalize())

# Make All UPPERCASE
print(s.upper())

# Make all lower
print(s.lower())

# Swap Case
print(s.swapcase())

# Replace method
print(s.replace('aleykum','aleyqum'))

# Count substrings
sub = 'a'
print(s.count(sub))

# Starts with
print(s.startswith('selam'))

# Ends with
print(s.endswith('m')) #False it ends with '!'

# Split into a list
print(s.split())

# Find position
print(s.find('y'))

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())

