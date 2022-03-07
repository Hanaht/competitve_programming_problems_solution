
a=int(input())
x=[int(i)for i in input().split()]
for i in range(1,len(x)):
    for j in range(x[i],0,-1):
        c=x[0]
        if x[i]%j==0:
            if c%j==0:
                d=c/j
                e=x[i]/j
                break
    print(str(int(d))+"/"+str(int(e)))
    