# cook your dish here
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    for item in arr:
        if item <=k:
            print(1,end='')
            k -= item
        else:
            print(0,end='')
    print()
