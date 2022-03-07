from math import gcd
n=int(input())
for j in range(n):
    c=int(input())
    a=[int(i)for i in input().split()]
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    if lcm>10**9:
         print("More than a billion.")
       
    else:
        print(lcm)

