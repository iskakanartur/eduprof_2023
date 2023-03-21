x=[]
s1=0
while True:
   r=int(input())
   print ('This is r...', r)
   if r==0:
       break
   else:
       x.append(r)
       print ("This is my list x....", x)
print ('*'*85)
s=(sum(x)/len(x))
print ('This is my s...', s)
print ('-'*85)
for i in x:
    s1=s1+(i-s)**2
    print ('This is my s1...', s1)
o=(s1/(len(x)-1))**(1/2)
print(o-0.000000000000001)