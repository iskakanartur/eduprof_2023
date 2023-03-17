
##### STRINGS ARE IMMUTABLE 
fruit = 'banana'
l = 'l'
print (fruit)

print (type (fruit))
print (l)

print (fruit[0])

print (fruit[5])
print (fruit[-1])
print ('*********************************')
print (fruit[0:])
fruit = 'Apple'
print (fruit)
print (fruit[2])
#fruit[2] = 'C'
######################### LIST S... LIST ARE MUTABLE!!!!!
my_list = list()
print (type(my_list))
my_list = ['Apple', 43, 'Robert', 'Oranges', 'Car']
print (my_list)
print(my_list[2]) 
my_list[2] = 'Juliet'
print(my_list[2])
print(my_list)
#####
my_list.append('dog')
print (my_list)
my_list.pop ()
print(my_list)
#my_list.append(54, 3)
my_list.insert(3, 'CAT')
print(my_list)
my_list.pop(3)
print(my_list)
print ('******************')

#################### LISTS SORT METHOD ################
# a list of numbers
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

#sort list in-place in ascending order
my_numbers.sort()

#print modified list
print(my_numbers)

# a list of strings
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

#sort list in-place in alphabetical order
programming_languages.sort()

#print modified list
print(programming_languages)

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

################## DICTIONARIES ###################
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_dict)
print(my_dict['brand'])
# print(my_dict['Ford'])
print (len(my_dict))
print(len(programming_languages))

print (my_dict.get("model"))
print (my_dict.keys())

my_dict['brand'] = 'Ferrari'
print (my_dict)
print(my_dict.keys())
print(my_dict.values())
print (my_dict.items())
print('************************************')
print (my_dict)

if "model" in my_dict:
  print("Yes, 'model' is one of the keys in the my_dictionary  dictionary")

print ('*************************')
print(my_dict.values())
print ('Ferrari' in my_dict.values())

############################### ITERATION  ###################
print (my_list)

for i in my_list:
  print (i)

print ("*"*100)
list1 = [10, 20, 30, 40, 50 ]

for chislo in list1:
  print (chislo + 5)



#### 
new_list = [x+1 for x in list1]
print (new_list)
###########
print (my_dict)

for key in my_dict.keys():
  print (key)

for key, value in my_dict.items():
  print ('KLYUCH ', key, 'ZHANCHENIE', value)
  

print ('***************************************')
######## Task 
ladies = ['Marina', 'Yulia', 'Anna', 'Snezhana']
gents = ['Yuri', 'Sergey', 'Vlad', 'Inokentii']

print (len(ladies), len(gents))

for lady ,gent  in zip(ladies, gents):
  print (lady, gent)

print ('###############################')

####################### TUPLE #######################
thistuple = ("apple", "banana", "cherry")
print(thistuple)
tup2 = ("apple", "apple", "banana", "cherry")
print (tup2)

print (tup2[2])
#tup2[2] = "ORANGE"

tup3 = ("apple", "apple", 45,  "banana", "cherry")
print (tup3)


