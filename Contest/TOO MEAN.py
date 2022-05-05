"""
- sum (x_i/k = A_1/s_1+...+A_n/s_n) k
- reforme the problem of an arr B_n
- we want the max of B_i = (A_i / K)
- sort the array B
- take k subsequence such that B_i - B_(n-k)
- prefix sum and then the remaining sum will be divided by (n - k)
"""
from sys import stdin
input = stdin.buffer.readline


def func():
	a.sort()

	total = sum(a)
	ans = 0
	extra = 0
	for i in range(n):
		avg = (total - extra) / (n - i)
		ans = max(ans, (avg + extra) / (i + 1))
		extra += a[~i]

	print(ans)


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	func()
