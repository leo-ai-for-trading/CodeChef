"""
max jump in 1 move is a + 3
max jump in 2 moves = 5 moves (3+2)
ans = (n/2)*2
"""
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = 2*(n//5)
    n%=5
    if n == 4: 
        ans += 2
    elif n!=0:
        ans += 1
    print(ans)
