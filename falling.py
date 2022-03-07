from math import sqrt
x=int(input())
fl=1
for i in range(x):
    p=(i*i)+x
    if sqrt(p)==int(sqrt(p)):
        print(i,int(sqrt(p)))
        fl=0
        break
if fl==1:
    print("impossible")