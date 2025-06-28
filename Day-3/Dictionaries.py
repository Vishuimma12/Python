
print("Welcome to the Dictionary Example!")

student = { 'Hermione': 'Gryffindor',
            'Harry': 'Gryffindor',  
            'Ron': 'Gryffindor',
            'Draco': 'Slytherin',
            'Luna': 'Ravenclaw',
            'Cedric': 'Hufflepuff' 
            }  # Dictionary of students and their houses
#hii

print("student are listed addresses:")
print(student['Hermione'])  # Gryffindor
print(student['Harry'])     # Gryffindor
print(student['Ron'])       # Gryffindor
print(student['Draco'])     # Slytherin
print(student['Luna'])      # Ravenclaw
print(student['Cedric'])    # Hufflepuff

# using a for loop to print each student and their house
print("\nUsing a for loop to print each student and their house:")
for students in student:
    print(students, "is in", student[students])
