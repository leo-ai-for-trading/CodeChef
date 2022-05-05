"""
- total sum of scores of N students = N*x
- p stundet score > avg
- p student score > x, maximise p
- p student score should be minimum possible
- it becomes p student score = x + 1
    if x + 1 <= M
-  so p = (n*x)/x+1 integer division
- the remainder of this can be distributed among the N-p student
"""
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,m,x = map(int,sys.stdin.readline().split())
    if x < m:
        print((n*x)//(x+1))
    else: print(0)
