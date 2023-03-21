# Just testing 
import string
import datetime 
import io

from pathlib import Path

data_folder = Path("/media/ayng/511132ba-8406-41a4-b633-0d9d60e15379/eduprof_2023/py/data/")
# file_to_open = io.open("test", mode="r", encoding="utf-8")
file_to_open = data_folder / "pushkin.txt"

#fhand = open(file_to_open,  mode="r", encoding="utf-8")
fhand = io.open(file_to_open,  mode="r", encoding="utf-8")

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

########################### PUSHKIN VISUALIZATION #######################
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

width = 0.5

myDictionary = {'я': 11, 'вас': 4, 'люблю': 2, '—': 7, 'хоть': 2, 'бешусь': 1, 'это': 1, 'труд': 1, 'и': 9}

plt.bar(myDictionary.keys(), myDictionary.values(), width, color='b')
plt.show()

