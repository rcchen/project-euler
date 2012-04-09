def digitSum(number,power):
	sum = 0
	while (number > 0):
		sum = sum + pow((number % 10),power)
		number = number / 10
	return sum	

total = 0

for i in range(2,10000000):	
	if (i == digitSum(i,5)):
		print i
		total = total + i

print total