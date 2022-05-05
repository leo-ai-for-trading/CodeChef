"""
- when u are incrementing a number u will decrement another one
- sum = constant for the reason above
- N/2 odd = x
- N/2 even = y
- |x - y| = 1 this is what we want
- x is presnt N/2 times and the same for y
- sum = x * N/2 + y * N/2
- if x > y, x = 1+y; y = y
- (1+y)*n/2 + y*n/2 = sum
x(y * n/2) + n/2 = sum
y * n = s - n/2
y = (s - n/2) / n
x = 1 + y
ELIF x < y:  y = 1 + x and x = (sum - n/2) / n
if (s - n/2) % n == 0:
  print(YES)
 else: print(NO)
"""
for i in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    s=sum(nums)*2
    if s%n==0 and(s//n)%2==1:
        print("YES")
    else:
        print("NO")
