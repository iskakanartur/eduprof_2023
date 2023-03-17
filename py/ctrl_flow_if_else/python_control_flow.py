##
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

print ('*'*100)

########################## ELIF 
x = 56
y = 34
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
    
print ('*'*100)

############ While ###########
i = 1
while i < 6:
  print(i)
  i += 1

print ('*'*100)

################# Break Statement 
i = 1
while i < 6:
  print(i)
  if i == 3:
    print ('WHooops i == 3 time to break ')
    break
  i += 1

print ('*'*100)

############## CONTINUE STATEMENT  -
# ##  With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print ('*'*100)

########### ELSE in WHile 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print ('*'*100)
############# More on FOR LOOPS

for i in [1, 2, 3, 4]:
    print(i, end=", ") # prints: 1, 2, 3, 4,

print ('*'*100)

# More complex example
for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x)

print ('*'*100)

############## The Range function in Python
## The start argument is the first value in the range. 
## If range() is called with only one argument, then Python assumes start = 0.

# Example with one argument
for i in range(5):
    print(i)

print ('*'*100)

## STEPS in RANGE
# In our final example, we use the range of integers 
# from -1 to 5 and set step = 2.

# Example with three arguments
for i in range(-1, 5, 2):
    print(i) 


