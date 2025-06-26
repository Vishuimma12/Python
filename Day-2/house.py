# match keyword

name = input("Enter your name: ")

# if name == "Harry":
#     print("Hello Harry, welcome to the Gryffindoor!")
# elif name == "Hermione":
#     print("Hello Hermione, welcome to the Gryffindoor!")
# elif name == "Ron":
#     print("Hello Ron, welcome to the Gryffindoor!") 
# elif name == "Draco":
#     print("Hello Draco, welcome to the Slytherin!") 
# else:
#     print("Hello, welcome to the Hogwarts!")


# Using match-case statement (Python 3.10+)
# match-case is a structural pattern matching feature introduced in Python 3.10.
match name:
    case "Harry":
        print("Hello Harry, welcome to the Gryffindoor!")
    case "Hermione":
        print("Hello Hermione, welcome to the Gryffindoor!")
    case "Ron":
        print("Hello Ron, welcome to the Gryffindoor!") 
    case "Draco":
        print("Hello Draco, welcome to the Slytherin!") 
    case _:
        print("Hello, welcome to the Hogwarts!")  # default case  