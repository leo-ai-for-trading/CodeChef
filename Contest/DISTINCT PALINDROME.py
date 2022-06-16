"""
if n < 2x - 1: ans = no
else: ans = yes
iterate from 1 to x-1 and change i position from start
"""

def solve():
    n,x = map(int,sys.stdin.readline().split())
    mlen = 2*x - 1
    if n < mlen:
        print(-1)
        return
    ans = ['a'for i in range(n)]
    for i in range(1,x):
        ans[i-1] = chr(ord('a')+i)
        ans[n-1] = chr(ord('a')+i)
    print("".join(ans))

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    (solve())
