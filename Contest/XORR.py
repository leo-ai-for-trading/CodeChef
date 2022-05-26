"""
- using dict to store the frequence
- xor the a[i] with b[i] and add the result into the freq
- ans += (i*(i-1))//2
"""

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    freq = dict()
    for i in range(0,n):
        if a[i]^b[i] in freq.keys():
            freq[a[i]^b[i]]+=1
        else:
            freq[a[i]^b[i]]=1
    ans = 0
    for i in freq.values():
        ans += (i*(i-1)//2)
    print(ans)
