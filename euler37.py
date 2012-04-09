import math

def isprime(num):
	if (int(num) == 1):
		return 0
	for i in range(2,int(math.floor(math.sqrt(int(num))))+1):
		if (int(num) % i == 0):
			return 0
	return 1

def lefttrunc(num):
	for i in range(0,len(str(num))):
		if (not isprime(str(num)[i:])):
			return 0
	return 1	
	
def righttrunc(num):
	for i in range(1,len(str(num))+1):
		if (not isprime(str(num)[:i])):
			return 0
	return 1

count = 0
total = 0
curr = 10

while (count < 11):
	if (lefttrunc(curr) and righttrunc(curr)):
		print curr
		total = total + curr
		count = count + 1
	curr = curr + 1

print total