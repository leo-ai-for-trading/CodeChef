# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    if (((n %2)) and ((m %2))):
        print('NO')
    else:
        print('YES')
