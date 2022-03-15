# cook your dish here
T = int(input())
for tc in range(T):
	# Read integers a and b.
    (a,b,c) = map(int,input().split(' '))
    #a = int(input())
    #ans = 4
    print(max((a,b,c)))
