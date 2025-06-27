
print("Welcome to Hogwarts!")

student = ['Hermione', 'Harry', 'Ron'] # List of students

print(student[0])  # Hermione
print(student[1])  # Harry
print(student[2])  # Ron


# # using a for loop to print each student
print("\nUsing a for loop to print each student:")
for students in student:
    print(students)


print("\nUsing a for loop with range to print each student:")
for i in range(len(student)):
    print(i+1, student[i])

