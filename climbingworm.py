a,b,c=[int(j)for j in input().split()]
cnt=1
if a<c:
    i=a
    while i<c:
        i=i-b
        i+=a
        cnt+=1
print(cnt)

