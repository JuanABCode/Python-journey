# Restaurant Order System

print("Dinnning in has a 8.75% tax")

print("----------- Menu -----------")
print("Ramen:                $19.99")
print("Burger:               $15.00")
print("Soup:                 $12.99")
print("Cake:                 $35.00")
print("Golden Steak:        $199.99")


menu = input("What would you like to eat: ").strip().lower()
quantity = int(input("How many are you buying: "))
experience = input("Are you dinning in (DI) or dinning out (DO):").strip().lower()

tax = 0.0875

if menu == "ramen":
    price = 19.99
    subtotal = price * quantity
    tax_amount = subtotal * tax
    total = subtotal + tax_amount
    string_subtotal = f"${subtotal:,.2f}"
    string_quantity = f"{quantity:,}"
    string_tax_amount = f"${tax_amount:,.2f}"
    string_total = f"${total:,.2f}"
    if experience == "di":
        print("---------- RECEIPT ----------")
        print(f"Ramen:{string_subtotal:>23}")
        print(f"Quantity:{string_quantity:>20}")
        print(f"Tax amount:{string_tax_amount:>18}")
        print(f"Total:{string_total:>23}")
        print("-----------------------------")
    elif experience == "do":
        print("---------- RECEIPT ----------")
        print(f"Ramen:{string_subtotal:>23}")
        print(f"Quantity:{string_quantity:>20}")
        print("-----------------------------")
    else:
        print("INVALID RESPONSE")
elif menu == "burger":
    price = 15.00
    subtotal = price * quantity
    tax_amount = subtotal * tax
    total = subtotal + tax_amount
    string_subtotal = f"${subtotal:,.2f}"
    string_quantity = f"{quantity:,}"
    string_tax_amount = f"${tax_amount:,.2f}"
    string_total = f"${total:,.2f}"
    if experience == "di":
        print("---------- RECEIPT ----------")
        print(f"Burger:{string_subtotal:>22}")
        print(f"Quantity:{string_quantity:>20}")
        print(f"Tax amount:{string_tax_amount:>18}")
        print(f"Total:{string_total:>23}")
        print("-----------------------------")
    elif experience == "do":
        print("---------- RECEIPT ----------")
        print(f"Burger:{string_subtotal:>22}")
        print(f"Quantity:{string_quantity:>20}")
        print("-----------------------------")
    else:
        print("INVALID RESPONSE")
elif menu == "soup":
    price = 12.99
    subtotal = price * quantity
    tax_amount = subtotal * tax
    total = subtotal + tax_amount
    string_subtotal = f"${subtotal:,.2f}"
    string_quantity = f"{quantity:,}"
    string_tax_amount = f"${tax_amount:,.2f}"
    string_total = f"${total:,.2f}"
    if experience == "di":
        print("---------- RECEIPT ----------")
        print(f"Soup:{string_subtotal:>24}")
        print(f"Quantity:{string_quantity:>20}")
        print(f"Tax amount:{string_tax_amount:>18}")
        print(f"Total:{string_total:>23}")
        print("-----------------------------")
    elif experience == "do":
        print("---------- RECEIPT ----------")
        print(f"Soup:{string_subtotal:>24}")
        print(f"Quantity:{string_quantity:>20}")
        print("-----------------------------")
    else:
        print("INVALID RESPONSE")
elif menu == "cake":
    price = 35.00
    subtotal = price * quantity
    tax_amount = subtotal * tax
    total = subtotal + tax_amount
    string_subtotal = f"${subtotal:,.2f}"
    string_quantity = f"{quantity:,}"
    string_tax_amount = f"${tax_amount:,.2f}"
    string_total = f"${total:,.2f}"
    if experience == "di":
        print("---------- RECEIPT ----------")
        print(f"Cake:{string_subtotal:>24}")
        print(f"Quantity:{string_quantity:>20}")
        print(f"Tax amount:{string_tax_amount:>18}")
        print(f"Total:{string_total:>23}")
        print("-----------------------------")
    elif experience == "do":
        print("---------- RECEIPT ----------")
        print(f"Cake:{string_subtotal:>24}")
        print(f"Quantity:{string_quantity:>20}")
        print("-----------------------------")
    else:
        print("INVALID RESPONSE")
elif menu == "golden steak":
    price = 199.99
    subtotal = price * quantity
    tax_amount = subtotal * tax
    total = subtotal + tax_amount
    string_subtotal = f"${subtotal:,.2f}"
    string_quantity = f"{quantity:,}"
    string_tax_amount = f"${tax_amount:,.2f}"
    string_total = f"${total:,.2f}"
    if experience == "di":
        print("---------- RECEIPT ----------")
        print(f"Golden Steak:{string_subtotal:>16}")
        print(f"Quantity:{string_quantity:>20}")
        print(f"Tax amount:{string_tax_amount:>18}")
        print(f"Total:{string_total:>23}")
        print("-----------------------------")
    elif experience == "do":
        print("---------- RECEIPT ----------")
        print(f"Golden Steak:{string_subtotal:>16}")
        print(f"Quantity:{string_quantity:>20}")
        print("-----------------------------")
    else:
        print("INVALID RESPONSE")
else:
    print("INVALID RESPONSE")