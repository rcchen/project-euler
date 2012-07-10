def repeating_digits(num):
	start = 10
	count = 1
	while (start % num != 1 and start % num != 0):
		start = (start *10 )% num
		count += 1
	return count

def is_prime(num):
	for foo in range(2,num):
		if (num%foo == 0):
			return 0
	return 1

highest = 0
thenumber = 0
for x in range(3,1000):
	if (is_prime(x)):
		repeat = repeating_digits(x)
		if (repeat > highest):
			highest = repeat
			thenumber = x

print highest