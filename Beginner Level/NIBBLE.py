# cook your dish here
T = int(input())
for tc in range(T):
	# Read integers a and b.
    #(a,b) = map(int,input().split(' '))
    a = int(input())
    ans = a % 4
    print('good') if ans == 0 else print('not good')
    
