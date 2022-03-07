x=int(input())
lst=[]
z=[]
a=''
for i in range(x):
    y=input()
    lst.append(y)
    z.append(y)
z=sorted(z)
x=''
for i in range(len(z)-1,0,-1):
    x+=z[i]
x+=z[0]
lst="".join(lst)
z="".join(z)
if z==lst:
    print("INCREASING")
elif x==lst:
    print("DECREASING")
else:
    print("NEITHER")