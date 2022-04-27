import math
    #if n is odd: x + y = n + 1
    #pattern: n = 2 ^ odd will be not allowed, so it is equal to 1
    #pattern: 2 ^ (odd - even) = 2 ^ odd -> answer = - 1
    #pattern: n = k^2 where k is even -> x + y = k + 2 and it is even
    #pattern: if n == 2: ans = 0
    # if n is odd ans = 1
    #if n = 2^odd * x ans is -1
    #if n is a perfect square: ans is = 1
    #if n is not a square, ans = 2
for kp in range(int(input())):
    n = int(input()) 
    def prime2(n):
        d2 = {}
        while n % 2 == 0:
            if(2 not in d2):
                d2[2] = 1
            else:
                d2[2] = d2[2] + 1
            n = n // 2
        return(d2)    
    def isPerfectSquare(x):
        if(x >= 0):
            sr = int(math.sqrt(x))
            return ((sr*sr) == x)
        return false
    if(n==1):
        print(0)
    elif(n%2!=0):
        print(1)
    elif(prime2(n)[2]%2!=0):
        print(-1)
    elif(isPerfectSquare(n)==1):
        print(1)
    else:
        print(2)

            
        
        
        
