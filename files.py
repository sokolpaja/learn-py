# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile = open('my-file.txt','w') # creating a file like open, and the 'w' is to write method

# some info and methods
print('Name: ',myFile.name)
print('closed: ',myFile.closed) # checked if it is closed or opened in our script here
print('mode: ',myFile.mode)

# Write to the file
myFile.write('I like coding')
myFile.write(' and learning new techs')
myFile.close()
print('closed: ',myFile.closed) # checked if it is closed or opened in our script here

# Append to file
myFile = open('my-file.txt','a') # creating a file like open, and the 'w' is to write method
myFile.write(' this is new append line')
myFile.close()


# Read to file
myFile = open('my-file.txt','r') # creating a file like open, and the 'w' is to write method
text = myFile.read(50) # read 50 chars from the file
myFile.close()
print(text)

