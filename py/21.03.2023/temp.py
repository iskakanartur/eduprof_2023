# Python Program to
# demonstrate union of
# two sets

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|"
# operator
population = people|dracula

print("\nUnion using '|' operator")
print(population)


#################################### INTERSECTION 
# Python program to
# demonstrate intersection
# of two sets

print ('*******************************************************')

set1 = set()
set2 = set()

for i in range(5):
	set1.add(i)

for i in range(3,9):
	set2.add(i)
	
print (set1, set2)

# Intersection using
# intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using
# "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)
