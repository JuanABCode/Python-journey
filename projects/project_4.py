# Weather Advisor or Receipt Generator

decision = input("Weather Advisor (1) or Receipt Generator (2): ").strip().lower()

if decision == "1":
    temperature = float(input("What is the temperature: "))
    is_raining = input("Is it raining outside (Y, N): ").strip().lower()
    is_sunny = input("Is it sunny outside (Y, N): ").strip().lower()
    is_snowing = input("Is it snowing outside (Y, N): ").strip().lower()

    if is_snowing == "y" and is_raining == "y":
        print("Stay Home Its cold or wet outside\n")
    elif is_sunny == "y" and temperature >= 70 and is_raining == "n":
        print("Its great outside\n")
    elif temperature <= 32 or is_snowing == "y":
        print("Wear a jacket\n")
    else:
        print("Up to you :)\n")

elif decision == "2":
    item = input("What Item are you buying: ").strip().title()
    price = float(input("How much is the item: $"))
    quantity = int(input("How many did you buy: "))
    is_student = input("Are you a student (Y, N): ").strip().lower()

    student_discount = 0.10
    tax = 0.0875

    subtotal = price * quantity

    discount_amount = 0
    if is_student == "y":
        discount_amount = subtotal * student_discount
    elif is_student != "n":
        print("Invalid Response")
        exit()

    total = subtotal - discount_amount
    tax_amount_discount = 0
    tax_amount_no_discount = 0

    if total > 50:
        tax_amount_discount = total * tax
        tax_amount_no_discount = subtotal * tax

    total_after_tax_with_discount = total + tax_amount_discount
    total_after_tax_with_no_discount = subtotal + tax_amount_no_discount

    string_price = f"${price:,.2f}"
    string_subtotal = f"${subtotal:,.2f}"
    string_total = f"${total:,.2f}"
    string_tax = f"{tax:.2%}"
    string_tax_amount_no_discount = f"${tax_amount_no_discount:,.2f}"
    string_tax_amount_discount = f"${tax_amount_discount:,.2f}"
    string_total_after_tax_with_no_discount = f"${total_after_tax_with_no_discount:,.2f}"
    string_total_after_tax_with_discount = f"${total_after_tax_with_discount:,.2f}"
    string_discount_amount = f"${discount_amount:,.2f}"

    if is_student == "y":
        print("For being a student you get a 10% discount\n")
        print("If total after discount is over $50, there is a 8.75% tax\n")
        print("-------------------- RECEIPT --------------------")
        print(f"Item: {item:>43}")
        print(f"Price: {string_price:>42}")
        print(f"Quantity: {quantity:>39}")
        print(f"Total: {string_subtotal:>42}")
        print(f"Discount amount: {string_discount_amount:>32}")
        print(f"Total after discount: {string_total:>27}")

        if total > 50:
            print(f"Tax: {string_tax:>44}")
            print(f"tax amount: {string_tax_amount_discount:>37}")
            print(f"Total after tax amount: {string_total_after_tax_with_discount:>25}")

        print("-------------------------------------------------")

    elif is_student == "n":
        print("If total after is over $50, there is a 8.75% tax\n")
        print("-------------------- RECEIPT --------------------")
        print(f"Item: {item:>43}")
        print(f"Price: {string_price:>42}")
        print(f"Quantity: {quantity:>39}")
        print(f"Total: {string_subtotal:>42}")

        if total > 50:
            print(f"Tax: {string_tax:>44}")
            print(f"tax amount: {string_tax_amount_no_discount:>37}")
            print(f"Total after tax amount: {string_total_after_tax_with_no_discount:>25}")

        print("-------------------------------------------------")

else:
    print("Invalid Response")
