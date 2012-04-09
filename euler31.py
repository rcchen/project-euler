coins = [200,100,50,20,10,5,2,1]

count = 0
discovered = []

def combinations(coin,total,combo):
	global count
	if (total == 0):
		count = count + 1
		print "foundone"
		return
	if (total < 0):
		return
	for another in coins:
		combinations(another,total-another)

for coin in coins:
	
	combinations(coin,20-coin,combo)

print count		
