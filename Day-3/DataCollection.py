# This code defines a list of dictionaries, where each dictionary represents a student
# with their name, house, and patronus. It then prints out the details of each student.
print("Welcome to the Hogwarts Student List!")
students = [
  {"Name": "Hermione", "House": "Gryffindor","Patronus": "Otter"},
  {"Name": "Harry", "House": "Gryffindor","Patronus": "Stag"},
  {"Name": "Ron", "House": "Gryffindor","Patronus": "Jack Russell Terrier"},
  {"Name": "Draco", "House": "Slytherin","Patronus": None},
  {"Name": "Luna", "House": "Ravenclaw","Patronus": "Hare"},
  {"Name": "Cedric", "House": "Hufflepuff","Patronus": None}
]

# Print the details of each student

for student in students:
    print(student['Name'],student['House'],student['Patronus'], sep=", ")  # each student's details are printed in a single line with commas separating the values

#Optimization: Using a single print statement
print("\nUsing a single print statement:")
for student in students:
    print(f"{student['Name']}, {student['House']}, {student['Patronus']}")  # using f-string for better readability 
    
