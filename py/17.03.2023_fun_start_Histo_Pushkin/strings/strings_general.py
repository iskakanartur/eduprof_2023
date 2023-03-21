##  STRING The startswith() and endswith() String Methods
print ('Hello world!'.startswith('Hello'))

print ('Hello world!'.endswith('world!'))

### Join method ##
', '.join(['cats', 'rats', 'bats'])
# print (', '.join(['cats', 'rats', 'bats']))

my_list = ['cats', 'rats', 'bats']
print (', '.join(my_list))
print ('*'*100)
################### Justifying Text with rjust(), ljust(), and center() ##############
'Hello'.rjust(10)
print ('Hello')
print ('Hello'.rjust(10))
print ('Hello'.ljust(10))
print ('Hello'.rjust(20, '*'))
print ('Hello'.ljust(20, '-'))
print ('Hello'.center(20))
print ('Hello'.center(20, '='))
print ('*'*100)
################################# DIFFERENT STRIPS ###########################
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
#print("of all fruits", txt, "is my favorite")

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print (spam.strip('ampS'))
