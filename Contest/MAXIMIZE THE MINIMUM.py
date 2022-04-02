"""
- delete k min elements from the list
- ans = the next largest element we have in the list
- 1 2 1 6 4 1, k = 3
delete all the ones (because u can do k-times the delete operation; than substitute the the 2 on the first two 1 
and 4 to the last 1
2 2 2 6 4 4
ans = 2

1 2 1 6 4 1, k = 4 it will become
6 6 6 6 4 4 
ans = 4

k + 1 smallest element in the list
"""
def sol():

import sys
t = int(sys.stdin.readline()):
for _ in range(t):
  n, k = map(int,sys.stdin.readline().split())
  a = list(map,sys.stdin.readline().split())
  a.sort
  k = min(k, n -1)
  print(a[k])
