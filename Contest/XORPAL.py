"""
- if it end with "0" i'll do forward
- else: backward
- need to check the half from the start and from the half to the end
- taking min(ceil.(n/2)) for min number of operations if we have unequal un-pair: we can re-write this with (n+1)/2
- 
"""
t = int(input())
for _ in range(t):
  n = int(input())
  a = input()
  c = 0
  for i in range(0,n//2):
    c += (a[i]!=a[n-i-1])
   print((c+1)//2)
  
