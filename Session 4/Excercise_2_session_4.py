prices = {}

prices ["banana"] = 4
prices ["apple"] = 2
prices ["orange"]= 1.5
prices ["pear"] = 3

print(prices)

purchased_items = {
    "banana": 5,
    "orange":3,
    }

for k in purchased_items:

    print(k, ",", "quantity:", purchased_items[k], ",", "unit price:", prices[k])
total = 0
for item in purchased_items:
    price = purchased_items[item] * prices [item]
    total += price
print("The total price is: ","$",total, sep="")
