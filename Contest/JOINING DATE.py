
the number of candidate who change is equal to the tot number of group - grouè of candidate ho left the company
calculate the tot number of group = n/5 + (if n%5 we will add 0 else 1)
total groups = k/5 + (k%5 we add 0 if true else 1)
"""


import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    if (n%5) == 0:
        m = 0
    else: m = 1
    tot_gr = (n//5) + m
    if k%5 == 0:
        a = 0
    else: a = 1
    cur_gr = (k//5) + a
    print(tot_gr-cur_gr)


