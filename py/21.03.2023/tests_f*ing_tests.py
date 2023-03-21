##################### Программный тест. Списки и кортежи ###################



######## TEST 1
## В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

##  Input     3 4 5 2 1
##   EXPECTED 3 4 1 2 5

##### MY thoughts, I am bewildered, confused, perplexed, angry, resentful
##### Who the F*** needs this? WHy?


########## SOLUTION STRATEGY TEST 1
## MY SEARCH PATTERN               swap min and max element in a python list

def swap_min_max(l):
    max_value = max(l)
    min_value = min(l)

    # get all potential indices
    idx_min = [i for i,e in enumerate(l) if e==min_value]
    idx_max = [i for i,e in enumerate(l) if e==max_value]

    # replace values
    for idx in idx_min:
        l[idx] = max_value
    for idx in idx_max:
        l[idx] = min_value

    return l

print (swap_min_max([3, 4, 5, 2, 1]) )

print ('Jesus man, now the autograder refuses accept my answer. well well ')

####### SEARCH GOOGLE  print python list elements wihout brackets and commas
my_list = [1, 2, 3]
print(' '.join(str(x) for x in my_list))

###### SOOOOOOO God damn it man, we finally satisfiy that greedy IDIOT Autograder
###### and who the FFF*** Put together this test? I am wondering

my_list_for_that_idiotic_test = [3, 4, 5, 2, 1]
my_temp_variable = swap_min_max(my_list_for_that_idiotic_test)

print(' '.join(str(x) for x in my_temp_variable))

####### PUT TOGETHER EVERYTHONG FOR A CORRECT RESULT
print ('-'*100)

def swap_min_max(l):
    max_value = max(l)
    min_value = min(l)

    # get all potential indices
    idx_min = [i for i,e in enumerate(l) if e==min_value]
    idx_max = [i for i,e in enumerate(l) if e==max_value]

    # replace values
    for idx in idx_min:
        l[idx] = max_value
    for idx in idx_max:
        l[idx] = min_value

    return l

my_list_for_that_idiotic_test = [3, 4, 5, 2, 1]
my_temp_variable = swap_min_max(my_list_for_that_idiotic_test.copy())

print(' '.join(str(x) for x in my_list_for_that_idiotic_test)) #### why copy?
#### Try  WITHOUT a copy 
print(' '.join(str(x) for x in my_temp_variable))



######################### FULL WORKING BUTCHERED CODE FOR TEST 1
def swap_min_max(l):
    max_value = max(l)
    min_value = min(l)

    # get all potential indices
    idx_min = [i for i,e in enumerate(l) if e==min_value]
    idx_max = [i for i,e in enumerate(l) if e==max_value]

    # replace values
    for idx in idx_min:
        l[idx] = max_value
    for idx in idx_max:
        l[idx] = min_value

    return l

my_list_for_that_idiotic_test = [3, 4, 5, 2, 1]
my_temp_variable = swap_min_max(my_list_for_that_idiotic_test.copy())


print(' '.join(str(x) for x in my_list_for_that_idiotic_test))
print(' '.join(str(x) for x in my_temp_variable))

############################ F ing END of it


###################################### Программный тест. Вложенные списки ###########################



print ('-_-'*45)





print ('-'*100)

######## Проверьте, является ли двумерный массив симметричным относительно главной диагонали. 
# Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива 
# в правый нижний.

##### OKAYYYY WHAT THE HELL is 2d array? huh?
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

N = 5
ar = [0]*N
print(ar)

# Example 2: Creating a 1d list using  List Comprehension
N = 5
arr = [0 for i in range(N)]
print(arr)

print ('-'*100)

## Method 2 Creating a 2-D list Example 1: Naive Method
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

print ('-'*100)

## Example 2: Using List Comprehension
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

print ('-'*100)
# Example 3: Using empty list
arr=[]
rows, cols=5,5
for i in range(rows):
	col = []
	for j in range(cols):
		col.append(0)
	arr.append(col)
print(arr)

print ('-'*100)

############################## NOW TEST SOLUTION ############
## SEARCH TERM check diagonals 2d array python

board =  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# You can get one diagonal with:

t = [r[i] for i, r in enumerate(board)]
print (t)

## And the opposite diagonal with:
tt = [r[-i-1] for i, r in enumerate(board)]
print (tt)











