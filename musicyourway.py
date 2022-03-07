x=[str(i) for i in input().split()]
y=int(input())
lst=[]
c=0
for j in range(y):
    z=[str (k) for k in input().split()]
    lst.append(z)
a=int(input())
for i in range(a):
    b=input()
    print(" ".join(x))
    c=x.index(b)
    lst.sort(key=lambda lst:lst[c])
    for n in lst:
        kk=" ".join(n)
        print(kk)
    if i!=a-1:
        print()
    
    #print(lst)
    

