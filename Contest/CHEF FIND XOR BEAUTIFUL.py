from collections import Counter
k=int(input())
while k:
    k-=1
    t=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    f=[]
    for i in l:
        f.append(i&m)
    j=Counter(f)
    sum=0
    for i in j:
        sum+=j[i]**2
    print(sum)
