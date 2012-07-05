def squaresum(number):
	sum = 0
	while (number > 0):
		sum = sum + pow(number % 10,2)
		number = number/10
	return sum

def chain(number):
	curr = number
	while (curr != 1 and curr != 89):
		curr = squaresum(curr)
	return curr

count = 0
for i in range (1, 10000000):
	if (chain(i) == 89):
		count = count + 1
print count