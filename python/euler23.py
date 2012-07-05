import math

def numStatus(num):
	sum = 0
	for i in range(1,int(math.floor(math.pow(num,0.5)))+1):
		if (num % i == 0):
			sum += i
			if (i != 1 and i != (num/i)):
				sum += (num/i)
	if (sum == num):
		return 0 # perfect
	elif (sum < num):
		return -1 # deficient
	else:
		return 1 # abundant

abundant_numbers = [];

for j in range(1,28124):
	if (numStatus(j) == 1): # abundant number
		abundant_numbers.append(j)

sums_found = [];
for m in range(0,len(abundant_numbers)):
	for n in range(1,len(abundant_numbers)):
		temp_sum = abundant_numbers[m] + abundant_numbers[n]
		if (temp_sum not in sums_found):
			sums_found.append(temp_sum)

final_sum = 0
for r in range(1,28124):
	if (r not in sums_found):
		final_sum += r

print final_sum
