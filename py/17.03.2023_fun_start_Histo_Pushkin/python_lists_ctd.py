############################### DIFFERENT APPROACHES SAME TASK . Append and Concat  ###############

#### ORIGINAL VERSION 
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation Mthod 
    # catNames.append(name)  # List append Method 
print('The cat names are:')
for name in catNames:
    print(' ' + name)



print ('*'*150)
print (catNames)
print ('-'*150)


#################### DEMONSTRATION OF THE DIFF METHOD 

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    # catNames = catNames + [name] # list concatenation
    catNames.append(name)
print('The cat names are:')
for name in catNames:
    print(' ' + name)

####### Print Cat Names List Method #########

#for i in catNames:
    #print(i)

#for x in range(len(catNames)):
    # print (catNames[x])


print ('*'*150)
print (catNames)

print ('-'*150)

###############################################