# string Indexing

credit_number = "1234-5678-9012-3456"

#print(credit_number[0])
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[5:])
# it would go backwards from the string  = 6
#print(credit_number[-1:])
# start / end / step it step in 2 characters
#print(credit_number[::2])

# step in negatives makes it so its backwards
reverse = credit_number[::-1]

print(reverse)

last_digits = credit_number[-4:]

print(f"****-****-****-{last_digits}")