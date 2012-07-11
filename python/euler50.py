import math

def isPrime(num):
	if (num == 2):
		return 1
	for x in range (2, (int)(math.sqrt(num)+1)):
		if (num % x == 0):
			return 0
	return 1

highestNum = 0
numTerms = 0
highestSum = 0

for start in range (2, 50000):
	if (isPrime(start)):
		curSum = 0
		curCount = 0
		for x in range (start, 50000):
			if (isPrime(x)):
				curSum += x
				curCount += 1
				if (curSum > 1000000):
					break
				if (isPrime(curSum) and curCount > numTerms):
					highestNum = start
					numTerms = curCount
					highestSum = curSum
					#print "New values: " + str(highestNum) + " " + str(numTerms) + " " + str(highestSum)

print str(highestNum) + " " + str(numTerms) + " " + str(highestSum)