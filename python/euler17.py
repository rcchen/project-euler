# letter count corresponding to index
ones = [0,3,3,5,4,4,3,5,5,4]
teens = [3,6,6,8,8,7,7,9,8,8] #+10
tens = [0,3,6,6,5,5,5,7,6,6]

def HundredsCount(num):
	return 7 + ones[num/100]

def TensCount(num):
	return tens[num/10] 

def TeensCount(num):
	return teens[num-10]

def AssembledNumberCount(num):
	temp = 0
	if (num > 100):
		temp += HundredsCount(num)
		temp += 3
	num = num % 100
	if (num < 10):
		return (temp + ones[num])
	if (num < 20 and num >= 10):
		return (temp + TeensCount(num))
	temp += TensCount(num)
	num = num % 10
	return (temp + ones[num])

def LetterCount(num):
	if (num < 10):
		return ones[num]
	if (num >= 10 and num < 20):
		return TeensCount(num)
	if (num % 100 == 0):
		return HundredsCount(num)
	if (num % 10 == 0 and num < 100):
		return TensCount(num)
	return AssembledNumberCount(num)

sum = 0
for foo in range (1,1000):
	sum += LetterCount(foo)
sum += 11
print "Total: " + str(sum)
