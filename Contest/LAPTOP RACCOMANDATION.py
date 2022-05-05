# cook your dish here
from collections import Counter
a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    if b==1:
        print(c[0])
    else:
        d=Counter(c)
        d=dict(sorted(d.items(), key=lambda item: item[1]))
        #print(d)
        m=list(d.values())
        if m[-1]==m[-2]:
            print("CONFUSED")
        else:
            print(list(d.keys())[-1])
