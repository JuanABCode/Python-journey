# Word Reverser + Analyzer

word = input("Enter a word (Type quit to quit): ").strip().lower()


while word != "quit":
    

word = word[::-1]

first_letter = word[0]
last_letter = word[-1]

print(word)
print(first_letter)
print(last_letter)