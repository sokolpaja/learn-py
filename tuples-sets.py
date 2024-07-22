#  A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Create a Tuiple
fr = ('molle','banana','orange')

fr2 = tuple(('molle','banana','orange'))

# When the tuple has only 1 element it is like this:
# with a comma(,), after the first element
fr3 = ('orange',)

print(type(fr),type(fr2))

# Get value(just like list)
print(fr[2])

# Can not change value
# fr[0]= 'Pear' #TypeError: 'tuple' object does not support item assignment

# Delete a tuple
del fr3
# print(fr3) #NameError: name 'fr3' is not defined.

# Get the length

print(len(fr))

# A SET is a collection which is unordered and un-indexed. No duplicate members

# create set

fr_set = {'molle','banana','mango'}

# check if is in set
print('molle' in fr_set)

# Add to set
fr_set.add('Grape')

# Remove
fr_set.remove('mango')

#Clear set
fr_set.clear()

# Delete set

# del fr_set #NameError: name 'fr_set' is not defined
 
print(fr_set)
