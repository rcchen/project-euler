def reverseNum(number):
	result = 0
	while (number > 0):
		result = result * 10 + number % 10
		number = number / 10
	return result

count = 0
for i in range(1,10000):
	sum = i
	tries = 0
	while (sum == i or sum != reverseNum(sum) and tries <= 50):
		sum = sum + reverseNum(sum)
		tries = tries + 1
		if (sum == reverseNum(sum)):
			break
	if (sum != reverseNum(sum)):
		print i
		count = count + 1

print "total count: " + str(count)