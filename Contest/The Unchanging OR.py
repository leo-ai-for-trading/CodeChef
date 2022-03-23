"""
1 -> 1
2->10
3->11

2 or 3 -> 10 or 11==3

f(4) = 1 | 2 | 3 | 4 where | is the OR operator
"""
# cook your dish here
import sys 

def pow2(bits):
    return 1 << bits

def max_num(bits):
    return pow2(bits+1)-1

def solution():
    N = int(sys.stdin.readline())
    bit_count = 0
    while N >> bit_count:
        bit_count += 1
    ans = 0
    for i in range(1,bit_count):
        ans += min(N,max_num(i)) - pow2(i)
        
    print(ans)

t = int(sys.stdin.readline())
while t > 0:
    t -= 1
    solution()
    
