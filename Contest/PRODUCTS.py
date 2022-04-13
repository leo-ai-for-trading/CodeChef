import sys
import itertools 


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    #ignore 0s
    #(n(n-1))//2
    cpos = 0
    cneg = 0
    for i in a:
        if i < 0:
            cneg += 1
        elif i > 0:
            cpos += 1
    print(cpos*(cpos - 1)//2 + cneg*(cneg - 1)//2)
