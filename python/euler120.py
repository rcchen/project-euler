import math

def Foo(a,n):
	if (n % 2 == 0):
		return 2
	else:
		return (int)(2*a*n%(math.pow(a,2)))

def FindMax(a):
	max = 0
	for x in range(1,(int)(math.pow(a,2))):
		bar = Foo(a,x)
		if (bar > max):
			max = bar
	return max

sum = 0
num = 1
cur = 0
for a in range(3,1001):
	if (num % 2 == 1):
		cur += 2
	num += 1
	sum += (a * cur)
print sum