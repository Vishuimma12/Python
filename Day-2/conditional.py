# Conditional statements are used to perform different actions based on different conditions.

# If statement
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > y: #---> If x is greater than y
    print(f"{x} is greater than {y}")
elif x < y: #---> If x is less than y
    print(f"{x} is less than {y}")
else: #---> If x is equal to y
    print(f"{x} is equal to {y}")   


# OR Using a single if statement
if x > y or x < y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")


# Not equal to operator
if x != y:  #---> If x is not equal to y
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

# And operator
score = int(input("Enter your score: "))
if score >= 90 and score <= 100:  #---> If score is between 50 and 100
    print("You passed the exam! `A`") 
elif score >= 80 and score < 90:
    print("You passed the exam! `B`") 
elif score >= 70 and score < 80:
    print("You passed the exam! `C`") 
elif score >= 60 and score < 70:
    print("You passed the exam! `D`")
elif score >= 50 and score < 60:
    print("You passed the exam! `E`")
else:
    print("You failed the exam! `F`") 

