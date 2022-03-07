x=int(input())
for i in range(x):
    input()
    y=int(input())
    c=0
    lst=[]
    if y==0:
        print('NO')
    else:
        for j in range(y):
            p=int(input())
            lst.append(p)
        c=sum(lst)
        if c%y==0:
            print("YES")
        else:
            print("NO")

