#  addition(+) substraing(-) multiplication(*) division(/)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

# Arithmetic Operators
print(f"Addition: {a + b}") 
# print("Ans"+int(input("Enter first number: ")) + int(input("Enter secind number: ")))  #---> addition

print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}") 
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")  #---> floor division
print(f"Modulus: {a % b}")  #---> modulus
print(f"Exponentiation: {a ** b}")  #---> exponentiation (a raised to the power of b)


# Comparison Operators
print(f"Is {a} equal to {b}? {a == b}")  #---> equal to
print(f"Is {a} not equal to {b}? {a != b}")  #---> not equal to
print(f"Is {a} greater than {b}? {a > b}")  # ---> greater than
print(f"Is {a} less than {b}? {a < b}")  #  ---> less than
print(f"Is {a} greater than or equal to {b}? {a >= b  }")  #---> greater than or equal to
print(f"Is {a} less than or equal to {b}? {a <= b}")  #---> less than or equal to


# Logical Operators 
print(f"Is {a} and {b} both non-zero? {a and b}")  #---> logical AND
print(f"Is {a} or {b} at least one non-zero? {a or b}")  #---> logical OR

print(f"Is {a} not zero? {not a}")  #---> logical NOT


# Assignment Operators    
a += 5  #---> a = a + 5 incrementing a by 5
print(f"After adding 5, a = {a}")
b -= 3  #---> b = b - 3 decrementing b by 3
print(f"After subtracting 3, b = {b}")  


# Floating Point Numbers
float_num = 5.522222 #---> float number
print(f"Float number: {float_num}")

round_num = round(float_num, 2)  #---> rounding the float number to 2 decimal places
print(f"Rounded number: {round_num}")


z=1000000000000;
print(f"{z:,}") #---> formatting the number with commas for readability it is a default feature of python
print(f"{z:,.2f}")  #---> formatting the number with commas and 2 decimal places


# def keyword
def hello():
    print("Hello, " + name)  #---> function to print hello message with user name

name = input("What is your name? ")
hello()
print(hello)