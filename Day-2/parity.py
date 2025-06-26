def main():
    x = int(input("Enter a number: "))
    if even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")  
def even(x):
    if x % 2==0:
        return True
    else:
        return False

main()