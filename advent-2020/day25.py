ll = open('day25.txt').read().splitlines()
n = 20201227
for i in range(n):
	if pow(7, i, n) == int(ll[0]):
		print(pow(int(ll[1]), i, n))