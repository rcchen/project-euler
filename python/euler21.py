upper = 10000
used = []

def divisorSum(number):
	sum = 0
	for i in range (1, number):
		if (number % i == 0):
			sum = sum + i
	return sum

total = 0
for i in range(1,upper):
	n1 = divisorSum(i)
	n2 = divisorSum(n1)
	if (n2 == i and n1 != i):
		print i
		total = total + i

print "sum is " + str(total)