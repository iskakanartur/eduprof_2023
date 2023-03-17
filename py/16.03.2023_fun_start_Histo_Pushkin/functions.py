my_list = [55, 4, -100, 33]
print (max(my_list))

t = '56'
print (type(t))

####################### Type conversion functions ###############
tt = int(t)
print (type(tt), t)

###################### rANDOM FUNCTION ###############
import random
for i in range(10):
    x = random.random()
    print(x)

################## USER DIFINED FUNCTIONS #################
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print_lyrics()

print ('*'*55)

print (type(print_lyrics))

################ TRIANGE AREA FUNCTION ###################
# area = b*h/2
def ploshad_triugolnika(base, height):
    b = base
    h = height
    area =  b*h/2
    return (area)

res = ploshad_triugolnika(12, 5)
print (res)

res1 = ploshad_triugolnika()


