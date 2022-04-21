from collections import Counter
"""
- a_i XOR a_j) AND x = 0
implies that (a_i AND x) XOR (a_j AND x) = 0
that implies A_i + A_j = 0
A_i == A_j
modify the array of the input to become A_i = a_i AND x
- find the counter of similar number
- map the array if you are in c++ to gent map<int,int>, where the first element is the element and the second is the frequency
- ans = sum(freq of i times freq of i element)
- iterate over the map and ans = sum of (p1 * second)^2
"""
k=int(input())
while k:
    k-=1
    t=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    f=[]
    for i in l:
        f.append(i&m)
    j=Counter(f)
    sum=0
    for i in j:
        sum+=j[i]**2
    print(sum)
