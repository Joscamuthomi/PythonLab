print("Welcome to my fruit shopping cart program")

fruits = []
prices = []
total =0

while True:
    fruit = input ("Enter fruit to buy:( q to quit)")
    
    if fruit.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {fruit} .$"))
        fruits.append(fruit)
        prices.append(price)

print("--YOUR CART--")

    
for price in prices:
    total +=price
    
print(f"Youve bought {fruits} for {total:.2f} ksh")