def hexagonal(number):
	return number * (number * 2 - 1)

def pentagonal(number):
	return (number * (3 * number - 1))/2

def triangle(number):
	return (number * (number + 1)) / 2

found = 0
start = 144
while (not found):
	numHexagonal = hexagonal(start)
	numPentagonal = 0
	countPentagonal = 0
	while (numPentagonal < numHexagonal):
		numPentagonal = pentagonal(countPentagonal)
		if (numPentagonal == numHexagonal):
			found = 1
			break
		countPentagonal += 1
	start += 1
print "found: " + str(hexagonal(start-1))