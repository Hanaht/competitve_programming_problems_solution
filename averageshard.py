x=int(input())
for k in range(x):
    f=0
    input()
    l=[]

    a,b=[int(i)for i in input().split()]
    q=[int(i)for i in input().split()]
    w=[int(i)for i in input().split()]
    n1=sum(q)/a
    n2=sum(w)/b
    for i in range(a):
        if q[i]<n1 and q[i]>n2:
            l.append(q[i])
       
    print(len(l))

    

