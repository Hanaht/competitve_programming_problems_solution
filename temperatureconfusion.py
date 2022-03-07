import math
x=input().split("/")
a=int(x[0])
b=int(x[1])

#print(a,b)
t=0
k=0
t=(5*a)-(160*b)
k=9*b
z=math.gcd(t,k)
#print(t,k)
r=0
s=0
r=int(t/z)
s=int(k/z)
print(str(r)+"/"+str(s))