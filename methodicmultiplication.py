w=input()
p=input()
ws=w.count("S")
ps=p.count("S")

l=ws*ps
if p!=0:
    for i in range(l):
        print("S(", end="")
    print("0", end="")
    for i in range(l):
        print(")", end="")
else:
    print("0")