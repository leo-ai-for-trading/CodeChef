# cook your dish here
t = int(input())
for _ in range(t):
    n,x,p = map(int,input().split())
    ans = (3*x) - (n-x)
    print('pass' if ans >= p else 'fail')
