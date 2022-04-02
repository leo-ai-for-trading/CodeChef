"""
- 2D list
- pick the max value
- max heap or priority queue and take the max element
- pick one element from the heap and increment the i element by 1
- repeat until i <= N - 1

"""
from heapq import *
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  
  arr = []
  for _ in range(n):
    arr.append([])
    
  for x, y in zip(a,b):
    arr[y].append(x)
 
  heap = []
  sm = 0
  ni = 0
  score = 0
  i = 0
  while i < n:
    for task in arr[i]: #represent all the task
      heapputsh(heap,task)
    if len(heap) == 0:
      break
    val = -heappop(heap)
    sm += val
    ni += 1
    score = max(score,sm/ni)
    i += 1
 print(score)
          
