"""
- if 1 are not adjiacent to each other we can solve it in just one move
- if they are all zeros no move required
- if the ones are adjency we need to make 2 moves
"""
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s =  str(sys.stdin.readline())
    ans = 0
    if s[0] == '1':
      ans = 1
    for i in range(1,n):
      if s[i] == '1' and s[i-1] == '1':
        ans = 2
        break
      elif s[i] == '1':
        ans = 1
     print(ans)
