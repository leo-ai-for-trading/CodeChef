'''
greatest common divisor approach

'''
from math import gcd
for _ in range(int(input)):
  n,q = map(int,input().split())
  while q > 0:
    q-=1
    g = gcd(x,y)
    x//=g
    y//=g
    ans = 0
    for i in range(2,a+1):
      if(i*i>a):
        break
       while(a%i==0):
        ans += i
        a//=i
     
       if (a>1):
        ans+=a
     print(ans)
