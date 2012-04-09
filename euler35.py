import math

def isprime(num):
    if (int(num) == 1):
        return 0
    for i in range(2,int(math.floor(math.sqrt(int(num))))+1):
        if (int(num) % i == 0):
            return 0
    return 1

def nextrotation(num):
	return num / 10 + (num % 10) * int(math.pow(10,len(str(num))-1))

lower = 2
upper = 1000000

count = 0

for i in range(lower,upper):
	curr = i
	circular = 1
	if (isprime(i)):
		curr = nextrotation(i)
		while (curr != i):
			if (not isprime(curr)):
				circular = 0
				break
			curr = nextrotation(curr)
		if (circular):
			print "found: " + str(i)
			count += 1

print "count: " + str(count)