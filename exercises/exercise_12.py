# Simple Tip Calculator

print("Tip minimum 15%")
bill = float(input("How much is the bill:$"))
amount = int(input("Number of people: "))
tip = float(input("What is the percentage of the tip %: "))

percentage_tip = tip / 100 # this makes the percentage into a decimal
subtotal = bill * percentage_tip # tip amount
total = subtotal + bill # total with the tip
split = total / amount # finds the amount split

string_bill = f"${bill:,.2f}"
string_percentage_tip = f"{percentage_tip:.2%}"
string_subtotal = f"${subtotal:,.2f}"
string_total = f"${total:,.2f}"
string_split = f"${split:,.2f}"


print("------------- RECEIPT -------------")
print(f"Bill:{string_bill:>30}")
print(f"People:{amount:>28}")
print(f"Tip Percentage:{string_percentage_tip:>20}")
print(f"Tip Amount:{string_subtotal:>24}")
print(f"Total:{string_total:>29}")
print(f'Split among {amount}:'f"{string_split:>21}")
print("-----------------------------------")