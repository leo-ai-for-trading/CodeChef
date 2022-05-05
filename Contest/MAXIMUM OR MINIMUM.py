"""
- reduce the count of 0 as much as possible by 1
- Bob want to reduce the count of ones in the list by 1
- if no zeros remain, print(1)
- else: print(0)
"""
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    L=[int(j) for j in input().split()]
    c1,c0=L.count(1),L.count(0)
    rem_numm=0
    if c1>=c0:
        rem_numm=1
    elif c0>c1:
        if abs(c0-c1)==1:
            if n%2==0:
                rem_numm=1
    print(rem_numm)
