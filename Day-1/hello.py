print("hello world!")

# name = input("What is your name? ")   #---> input function to get user input 'name' is a variable

# name = name.strip()  #---> removes leading and trailing spaces so that the output is clean...

# name = name.title()  #---> capitalize the first letter of the name

name = input("What is your name? ").strip().title()  #---> combining input, strip and title methods in one line

print("Hello, " + name) #---> print function to display output and name is a variable containing user input which is known as concatenation

# Reference: docs.python.org/3/library/functions.html

# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep = ' '  #---> separator between objects, default is space
# end = '\n'  #---> what to print at the end, default is newline

print("Hello," , end="")
print(name)
#---> using end="" to avoid newline after the first print

print("Hello,", name, sep=" ")  
#---> using sep=" " to specify the separator between objects, default is space

print(f'Hello, {name}') #---> using f-string for formatted string literals.

# generally we dont use like that {name} when we give extra space in the input, it will be printed as it is.
# To remove extra spaces we can use strip() method   (usend in line 5) 


# Split username into first and last name
first_name, last_name = name.split()  #---> split the name into first and last name
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")