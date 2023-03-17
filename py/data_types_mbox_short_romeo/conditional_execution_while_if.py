##
import os
x = 18
#y = 5
print (type(x))
print ('*')


if x > 0 :
    print('x is positive')
else :
    print ('X is not positive ')

print (os.getcwd())

###############
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

print ('**********************************************************************')

########################## ELIF 
x = 56
y = 34
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')