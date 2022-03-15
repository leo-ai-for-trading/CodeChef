# cook your dish here
T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a,b,c,d) = map(int,input().split(' '))
	ans = 'yes' if c*d >= a*b else 'no'
	print(ans)
