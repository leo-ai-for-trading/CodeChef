# cook your dish here
T = int(input())
while T > 0:
    a,b = map(int,input().split())
    print(0 if b > a else a//b)
    T -= 1
