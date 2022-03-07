t=int(input())
x=[int (j) for j in input().split()]
lst=[x[0]]
b=x[0]
for h in range (len(x)-1):
    
    if  b<x[h+1]:
        b=x[h+1]
        
        lst.append(b)
print(len(lst))
for y in lst:
    print(y,end=" ")


