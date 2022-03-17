# cook your dish here
from collections import Counter
t = int(input())
dr,sl = 'DRAGON','SLOTH'
for _ in range(t):
    dsa,toc,dm = list(map(int,input().split()))
    d = Counter({'dsa':dsa,'toc':toc,'dm':dm})
    sdsa,stoc,sdm = list(map(int,input().split()))
    s = Counter({'dsa': sdsa,'toc':stoc,'dm':sdm})
    if sum(d.values()) < sum(s.values()):
        print(sl)
    elif sum(d.values()) > sum(s.values()):
        print(dr)
    else:
        d.subtract(s)
        if d['dsa'] > 0:
            print(dr)
        elif d['dsa'] < 0:
            print(sl)
        else:
            if d['toc'] > 0:
                print(dr)
            elif d['toc'] < 0:
                print(sl)
            else:
                if d['dm'] > 0:
                    print(dr)
                elif d['dm'] < 0:
                    print(sl)
                else:
                    print('TIE')
