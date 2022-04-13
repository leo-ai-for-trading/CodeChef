# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n&1:
        if n==1 or n==3:
            print(-1)
        else:
            print("3 5 1 2 4",end=' ')
            for i in range(n,5,-1):
                print(i,end=' ')
            print()
    else:
        for i in range(1,n+1):
            print(n-i+1,end=' ')
        print()
