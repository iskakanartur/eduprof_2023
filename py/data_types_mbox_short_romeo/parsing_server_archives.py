##################### Notes on Mar 13 Lecture ################
## CONDITIONAL EXECUTION CH3 
## ITERATION CH 5 
## STRINGS  PY4E CH6
## LISTS PY4E CH 8  : !!! EXERCISES PAGE 106
## DICTIONARIES CH 9 





## Lists Parsing Lines Dr Chuck Lecture snapshot
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

print ('*'*100)

##### DICT IN LECTURE EXERCIESE ROMEO ADVANCED
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


