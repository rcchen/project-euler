def hexagonal(number):
	return number * (number * 2 - 1)

def pentagonal(number):
	return (number * (3 * number - 1))/2

def triangle(number):
	return (number * (number + 1)) / 2

hexstart = 144
#penstart = 165

while 1:
	hexagonal * 2

#temp = penstart
#while (pentagonal(temp) < hexagonal(hexstart)):
#	temp = temp + 1
#	if (pentagonal(temp) == hexagonal(hexstart)):
#		print pentagonal(temp)
#		break
#	if (pentagonal(temp) > hexagonal(hexstart)):
#		hexstart = hexstart + 1
#		penstart = penstart + 1
#		temp = penstart