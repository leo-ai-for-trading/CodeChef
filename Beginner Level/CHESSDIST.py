# cook your dish here
t = int(input())
while t > 0:
    (a,b,c,d) = [int(i) for i in input().split()]
    ans = [abs(a-c),abs(b-d)]
    
    print(max(ans))
    t -= 1
