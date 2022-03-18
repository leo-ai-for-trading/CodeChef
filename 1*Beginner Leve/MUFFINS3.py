# cook your dish here
import sys
import math
t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(math.floor(n/2+1))
