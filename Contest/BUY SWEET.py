    #effective_cost = a[i] - b[i]
    #sort all the value in this effective cost order
for _ in range(int(input())):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    c=list(map(int,input().split()))
    b = []
    m = l[0]
    for i in range(x):
        b.append([(l[i] - c[i]), i])
        if(l[i] < m):
            m = l[i]
    z = sorted(b)
    count = 0
    for i in z:
        a = i[1]
        if(y == 0 or y < m):
            break
        while y > 0:
            s = y // l[a]
            if(s == 0):
                break
            y -= s * l[a]
            count += s
            y += s * c[a]
    print(count)
