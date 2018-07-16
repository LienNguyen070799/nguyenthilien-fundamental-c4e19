prices = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
for key,value in prices.items():
    print(key,value)
for key, value in stock.items():
    print(key,value)
loop = True
while loop:
    fruit = input("fruit : ")
    if fruit in prices:
        print("prices: ",prices[fruit])
        print("stock: ",stock[fruit])
    else:
        print( "Not found")
        loop = False
total = 0
for fruit in stock :
    money = prices[fruit]*stock[fruit]
    print(fruit,":", money,"$")
    total += money
print("If I sold all of my food,I would make",total, "$")
