import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,x = (map(int,sys.stdin.readline().split()))
    #(x-a+x+a)//2
    ans = []
    for i in range(1,n//2+1):
        ans.append(x-i)
    if n%2 == 1:
        ans.append(x)
    for i in range(1, n//2+1):
        ans.append(x+i)
    print(*ans)
