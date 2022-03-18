# cook your dish here
import sys
t = int(input())
for _ in range(t):
    n,p,x,y= map(int,sys.stdin.readline().split())
    a= list(map(int,sys.stdin.readline().split()))
    #a == 1: elder person
    #a == 0: child
    ans = 0
    for i in range(p):
        if a[i] == 1:
            ans += y
        else:
            ans += x
    print(ans)
        
