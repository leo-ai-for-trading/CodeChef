# cook your dish here
t = int(input())
for tc in range((t)):
    a,b = map(int,input().split())
    ans = 21 - (a +b) 
    print(-1 if ans > 10 else ans)
    
