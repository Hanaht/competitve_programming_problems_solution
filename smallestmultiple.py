from math import gcd
while True:
    try:
        x=[int(i)for i in input().split()]
        lcm=x[0]
        for i in x[1:]:
            #print(i)
            lcm=lcm*i//gcd(lcm,i)
        print(lcm)
    except EOFError:
        break