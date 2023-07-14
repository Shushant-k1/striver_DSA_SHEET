# binary exponentation
def modularExponentiation(x, n, m):
	# Write your code here.
	p = bin(n)
	ans = 1
	for i in range(len(p)- 1, 1 , -1) :
		if int(p[i]) &  1 :
			ans = (ans * x ) %  m
		x = (x * x ) % m
	return ans % m
