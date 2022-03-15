# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for age in arr:
        if age >= 10 and age <= 60:
            count += 1
    print(count)
    
