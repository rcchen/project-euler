year = 1901
month = 1
dayofweek = 2
count = 0

def daysInMonth(month, year):
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		return 31
	if (month == 4 or month == 6 or month == 9 or month == 11):
		return 30
	if (month == 2 and year % 400 == 0 or year % 4 == 0):
		return 29
	return 28

while (year < 2001):
	dayofweek = (dayofweek + daysInMonth(month, year)) % 7
	month += 1
	if (month == 13):
		year += 1
		month = 1
	if (dayofweek == 0):
		count += 1

print count