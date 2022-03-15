T = int(input())
for tc in range(T):
	# Read integers a and b.
    (a,b) = map(int,input().split(' '))
    ans = a - b
    print('same') if ans == 0 else print('bike') if ans < 0 else print('car') 
	 
