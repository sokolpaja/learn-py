# A dictionary is a collection which is unordered, changeable and indexed. no duplicate members like objects or json

# Create Dictionary(dict)

person = {
    'first_name': 'Sokol',
    'last_name': 'Paja',
    'age':33
}

# Get the value

# print(person['first_name'])
# print(person.values())
# print(person.get('last_name'))

# Copy dist (like the spread(...) operator in js)
person2 = person.copy()

person2['city'] = 'Belsh'
# print(person2)

# Remove item

del(person['age'])
person2.pop('city')


# Clear Object(dict)
person.clear()

print(person,
      person2)

# Get length
print(len(person2))

# List of Dict (Array of Objects)

people = [
    {
    'first_name': 'Sokol',
    'last_name': 'Paja',
    'age':33
    },
    {
    'first_name': 'Sokol',
    'last_name': 'Paja',
    'age':39
    }
]

print(people[0]['age'])
print(people)