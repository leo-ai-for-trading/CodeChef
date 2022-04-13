t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if(n%2==1):
        print("NO")
        continue
    print("YES")
    ones=0
    for i in s:
        if(i=='1'):
            ones+=1
    zeros=n-ones
    if(zeros<ones):
        snew=""
        for i in s:
            if(i=='0'):
                snew+='1'
            else:
                snew+='0'
        s=snew
        t=ones
        ones=zeros
        zeros=t
    print(1, end=" ")
    diff=0
    curr=0
    for i in s:
        if(i=='0'):
            diff+=1
        else:
            diff-=1
        if(diff==(zeros-ones)//2):
            print(curr+1)
            break
        curr+=1
