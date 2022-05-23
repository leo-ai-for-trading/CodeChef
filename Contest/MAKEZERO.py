"""
- check in the arr where x^y is present and subtract it
- initialize the arr with 31 element because we are decompose 10^9 into 2^29
"""
def solve(arr):
    v=[0]*31
    for i in arr:
      for j in range(31):
        if i&(1<<j):v[j]=1
    ans = 0
    for j in v:
      if j: 
        ans += 1
    return ans
  
 t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  print(solve(arr))
