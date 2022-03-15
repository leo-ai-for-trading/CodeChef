# cook your dish here
T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = (a*2) + (b*4)
	print(ans)
