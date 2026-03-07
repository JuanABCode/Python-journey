# Grade Calculator

test_1 = float(input("What was your score on your first test: ")) 
test_2 = float(input("What was your score on your second test: ")) 
test_3 = float(input("What was your score on your third test: ")) 
test_4 = float(input("What was your score on your fourth test: ")) 
test_5 = float(input("What was your score on your fifth test: ")) 

average = (test_1 + test_2 + test_3 + test_4 + test_5) / 5

if average > 90:
    print(f"Your average for all 5 test is {average:.1f} and your grade is A")
elif average > 80:
    print(f"Your average for all 5 test is {average:.1f} and your grade is B")
elif average > 70:
    print(f"Your average for all 5 test is {average:.1f} and your grade is C")
elif average >= 60:
    print(f"Your average for all 5 test is {average:.1f} and your grade is D")
elif average < 60:
    print(f"Your average for all 5 test is {average:.1f} and your grade is F")
else:
    print("Invalid Response")
