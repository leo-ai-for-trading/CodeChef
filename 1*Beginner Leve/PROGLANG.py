# cook your dish here
t = int(input())
for _ in range(t):
    #A,B,A_1,B_1,A_2,B_2
    #first two integer are the required features
    A,B,a_1,b_1,a_2,b_2 = map(int,input().split())
    if ((A == a_1 and B == b_1) or (B == a_1 and A == b_1)):
        print(1)
    elif ((A == a_2 and B == b_2) or (B == a_2 and A == b_2)):
        print(2)
    else:
        print(0)
