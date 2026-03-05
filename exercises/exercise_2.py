# shopping cart

item = input("What Item are you buying: ")
price = float(input("How much is the item: $"))
quantity = int(input("How many are buying of that project: "))

total = price * quantity

print(f"You are buying {item} and each one is worth ${price} and you are buying {quantity} of them!")
print(f"The total is ${total:,.2f}")