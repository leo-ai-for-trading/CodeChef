T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a,b) = map(int,input().split(' '))
	ans = (a*10) + (b*5)
	print(ans)
