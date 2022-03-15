# cook your dish here
t = int(input())
for tc in range(t):
    a,b = map(int,input().split())
    ans = a // (b*2)
    print(ans)
