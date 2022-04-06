"""
- i and j pointers not adjacency between each other
- remove A_i and A_j 
- append A_i + A_j
- find min operations to make a good array
- if A will have all elements with parity = 1
    - A = 000111...111 count0, count1
    - odd + even = odd
    - decrement count0 by 1 and leave count1 as the same
    - ans = count0
- if A have all elements with parity = 0
    - A = 000...1111..11 count0, count1
    - odd + odd = even
    - we need to remove all the elements with parity = 1
    - count0 increase by 1 and decrese count1 by 2
    - ans = count1/2
    - if count1 is odd: at the end one 1 will remain
    - ans = count0
- sol(A,N):
    count0: number of even element
    count1: numeber of odd element
    if count1 % 2 == 1:
        print(count0)
    else:
        print(min(count0,count1/2))
"""

import sys

def solve(A,N):
    odd,even = 0,0
    for i in range(N):
        if A[i] & 1:
            odd += 1
        else:
            even += 1
    if odd & 1:
        print(even)
    else:
        print(min(even,odd//2))

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    solve(A,n)
