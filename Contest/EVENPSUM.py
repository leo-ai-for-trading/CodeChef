# cook your dish here
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    #count the possible value even in a and b
    a_even = a //2
    b_even = b //2
    a_odd = a -a_even
    b_odd = b - b_even
    ans = (a_even*b_even)+(a_odd*b_odd)
    print(ans)
