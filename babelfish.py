d={}
while True:
    try:
        x,y=[str(i)for i in input().split()]
        d[y]=x
    except:
        break
while 1:
    try:
        a=input()
        if a in d:
            print(d[a])
        else:
            print("eh")
    except:
            break