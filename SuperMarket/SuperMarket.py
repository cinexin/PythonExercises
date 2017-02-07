# My SuperMarket exercise! (fixed & augmented)

prices = {"banana":4, "apple":2,"orange":1.5,"pear":3}
stock = {"banana":6, "apple": 0, "orange": 32, "pear": 15}
groceries = ["banana","orange","apple"]

def visualizeStock():
	for item in prices:
	    print item
	    print "price: " + str(prices[item])
	    print "stock: " + str(stock[item])
def totalStockValue():
	total = 0
	for key in prices:
		total += stock[key]*prices[key]
	return total

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

visualizeStock()
print totalStockValue()	

print compute_bill(["banana", "orange", "apple", "banana"])
visualizeStock()
