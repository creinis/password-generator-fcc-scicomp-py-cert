# Password Generator Lecture

# Step 1

# A Python module is a file containing code designed to perform specific tasks. 
# The Python standard library contains many modules that you can import and use in your code. 
# You can achieve this by using the import statement followed by the name of the module.

#Start this project by importing the string module.

import string

# Step 2

# You can access the utilities defined inside the imported module through the dot notation. 
# The dot notation works by appending a dot followed by the utility name to the module name. 
# For example, here's how to access the ascii_lowercase constant:

import string


print(string.ascii_lowercase)
# Output: abcdefghijklmnopqrstuvwxyz

# In this project, you are going to use different constants from the string module.
# Declare a new variable called letters and assign string.ascii_letters to this variable.

letters = string.ascii_letters

# Step 3

#Declare two new variables named digits and symbols and assign them string.digits and string.punctuation, 
# respectively.

digits = string.digits
symbols = string.punctuation

# Step 4

# These three variables constitute the possible characters to choose from when generating the password.
# Just before them, add a comment saying Define the possible characters for the password.

# Step 5

# Now declare a variable named all_characters and assign it the result of concatenating your existing variables.

all_characters = letters + digits + symbols

# Step 6

#Your all_characters variable is a string formed by all lowercase and uppercase letters, 
# all the 10 digits and several special characters.

#Just before it, add a comment saying Combine all characters.

# Step 7

# Now print the all_characters variable to see what it looks like.

print(all_characters)
# Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Step 8

#It is a common convention to place import statements at the top of your code. 
# And additionally, in case of multiple import statements, sort them in alphabetical order to improve readability.

#At the top of your code, import the random module.

import random

# Step 9

# The random module contains a pseudo-random number generator. 
# Most of its functionalities depend on the random() function, 
# which returns a floating point number in the range between 0.0 (inclusive) and 1.0 (exclusive).

# Call the random() function and print the result.

print(random.random())

# Step 10

# The choice() function from the random module takes a sequence and returns a random item of the sequence.
# Modify your print() call to use the choice() function and pass all_characters as the argument.

print(random.choice(all_characters))

