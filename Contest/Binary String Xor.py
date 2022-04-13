def count0(s,n):
    c=0
    x=0
    for i in s:
        if(i=='0'):
            if(x==0):
                c+=1
        else:
            if(x==1):
                c+=1
                x=0
            else:
                x=1
    if(x==1):
        return 0
    return c

def count1(s):
    c=0
    for i in s:
        if(i=='1'):
            c+=1
    if(c==0):
        return 0
    return c

t=int(input())
for _ in range(t):
    n,k=[int(i) for i in input().split()]
    s=input()
    ones=count1(s)
    zeros=count0(s,n)
    if(zeros>=k):
        print("YES")
        continue
    d=ones-k
    if(d>=0 and (d%2==0)):
        print("YES")
        continue
    print("NO")
    
