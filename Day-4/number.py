def main():
    x = get_int("What is your favorite number? ")
    print(f"You entered: {x}")
  

def get_int(prompt):
    while True:
        try:  # try use to catch exceptions
            return int(input("Enter an integer: "))
        except ValueError:  # exception handling for ValueError
            pass  # If the input is not an integer, it will continue to prompt the user until a valid integer is entered     
main()



