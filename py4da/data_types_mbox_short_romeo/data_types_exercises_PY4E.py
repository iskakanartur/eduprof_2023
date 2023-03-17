############################### LIST EXERCISES #########################

###### LIST EXERCISE 1
## Write a program to open the file romeo.txt and read it line by line. For each line,
## split the line into a list of words using the split function.
## For each word, check to see if the word is already in a list. 
##If the word is not in the list, add it to the list.

## When the program completes, sort and print the resulting words in alphabetical order.

## Expected Output 
ex = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']


####### SOLUTION EX 1


fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst) 

print ('**'*100)


####### LIST EXERCISE 2

## Write a program to read through the mail box data and when you
## find line that starts with “From”, you will split the line into words using the split
## function.
##  We are interested in who SENT the message, which is the second word onthe From line.

## From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

## You will parse the From line and print out the second word for each From line,
## then you will also count the number of From (not From:) lines and print out a
## count at the end.

## EXPECTED OUTPUT 
## stephen.marquard@uct.ac.za
## louis@media.berkeley.edu

## cwen@iupui.edu
## There were 27 lines in the file with From as the first word


################# SOLUTION TO LISTS EX 2

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)

print ('*'*100)


###################################### DICTIONARY EXERCISES #########################


#### DICT EX 1
count = 0
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                        # Discards duplicates
        dictionary_words[word] = count      # Value is first time word appears

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')
print ('This is dictionary_words', dictionary_words)

print ('*'*100)

#### DICT EX 2

## Write a program that categorizes each mail message by which day of
## the week the commit was done. To do this look for lines that start with “From”,
## then look for the third word and keep a running count of each of the days of the week. 
# ## At the end of the program print out the contents of your dictionary (order
## does not matter).

## Sample Line:
##     From stephen.marquard@uct.ac.za Sat Jan
##     5 09:14:16 2008



##### SOLUTION TO DICT EX 2
dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print ('This is solution for DICT EX2')
print(dictionary_days)
print ('*'*100)

#### DICT EX 3

## Write a program to read through a mail log, build a histogram using
## a dictionary to count how many messages have come from each email address, and
## print the dictionary.

## SOLUTION to DICT EX 3
dictionary_addresses = dict()                   # Initializes the dictionary
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
        else:
            dictionary_addresses[words[1]] += 1     # Additional counts

print('This is the soulution for DICT EX 3', dictionary_addresses)

