def FindNumberPower(power):
	sum = 0
	i = 1
	foo = 0
	while (len(str(foo)) < power):
		foo = pow(i,power)
		if (len(str(foo)) == power):
			print str(power) + " " + str(foo)
			sum += 1
		i += 1
	return sum
	
finalsum = 0
for x in range(1,1000):
	finalsum += FindNumberPower(x)

print finalsum