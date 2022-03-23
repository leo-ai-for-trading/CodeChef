"""
better to find the number of zero and the number of ones
- take the min number 
- now use the min number to form a new string (2 zeros for example) and now add them the same number of zeros and 
- ans = 2*min(zeros,ones) + (zeros != ones) -> it will return 1 if it is True else 0
- 2*2+1 = 5
"""
# cook your dish here
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s =  str(sys.stdin.readline())
    zero = str.count(s,'1')
    ones = str.count(s,'0')
    ans = 2 * min(zero,ones) + (zero != ones) #the last one return 1 if True
    print(ans)
