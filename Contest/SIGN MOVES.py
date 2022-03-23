"""
- 0 is consider non negative coordinate
- pattern: first number is negative in output and second number is positive and so on
- if initial number is even: output is positive
- if initial number is odd: output is negative
- ans = (N+1)/2
"""
# cook your dish here
import sys 
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = (n+1)//2 
    print(- ans if n&1 else ans) #using the & operator to indicate the odd number
