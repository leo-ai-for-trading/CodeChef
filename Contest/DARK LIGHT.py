import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    #k=0: Off
    #k=1: On
    if k == 1:
        if n % 4 == 0:
            print("On")
        else:
            print("Ambigous")
    else:
        if n%4==0:
            print("off")
        else:
            print("On")
