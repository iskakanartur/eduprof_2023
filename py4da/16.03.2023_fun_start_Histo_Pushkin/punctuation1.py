#################### define punctuation BRUTAL METHOD !!! ###################
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

print ('*'*100)

############################# Built in method ##################

# import string library function 
import string 
    
# Storing the sets of punctuation in variable result 
result = string.punctuation 
    
# Printing the punctuation values 
print('This is my string punctutaion method', result) 

print ('*'*100)

########################### STACK EXAMPLE ###################

import string

# Thanks to Martijn Pieters for this improved version

# This uses the 3-argument version of str.maketrans
# with arguments (x, y, z) where 'x' and 'y'
# must be equal-length strings and characters in 'x'
# are replaced by characters in 'y'. 'z'
# is a string (string.punctuation here)
# where each character in the string is mapped
# to None
translator = str.maketrans('', '', string.punctuation)

# This is an alternative that creates a dictionary mapping
# of every character from string.punctuation to None (this will
# also work)
#translator = str.maketrans(dict.fromkeys(string.punctuation))

s = 'string with "punctuation" inside of it! Does this work? I hope so.'

# pass the translator to the string's translate method.
print(s.translate(translator))