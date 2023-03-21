n=int(input())
s=""
f=""
a=n*2-1
for i in range(1,n+1):
    if i<=n:
        for x in range(1,i+1):
            s=s+str(x)
        for j in range(i-1,0,-1):
            f=f+str(j)
        print(format(int(s+f),f'^%d' % a))
        s=""
        f=""
for i in range(n,1,-1):
    for x in range(1,i):
        s=s+str(x)
    for j in range(i-2,0,-1):
        f=f+str(j)
    print(format(int(s+f),f'^%d' % a))
    s=""
    f=""