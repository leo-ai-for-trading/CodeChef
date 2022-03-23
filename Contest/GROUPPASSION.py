"""
- ans = 2N - (x-1)
"""
# cook your dish here
# cook your dish here
import sys 
t = int(sys.stdin.readline())
for _ in range(t):
    n,x = map(int,sys.stdin.readline().split())
    ans = 2*n -x +1
    print(ans)
