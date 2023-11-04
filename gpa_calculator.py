# defining grade letters and GPA scores with variable
grade_letters = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0.0
}

while True:
# ask user to enter the total amount of grades which will provide error if user enters a non-numerical value
while True:
num_grades_input: str = input("Enter the number of grades: ")
num_grades_input.isdigit():
num_grades = int(num_grades_input)
break
else:
print('Invalid input. Please enter a numeric value.')

# setting variables for grade points and total grade points
grade_points = 0
total_grade_points = 0

# asking the user to enter each grade
for i in range(num_grades):
while True:
grade = input('Enter grade %d: ' % (i + 1)).upper()

# error protection to ensure grade is valid
if grade in grade_letters:
grade_points = grade_letters[grade]
total_grade_points += grade_points
break
else:
print('Invalid grade!')

# calculate the gpa number
gpa = total_grade_points / num_grades

# print the gpa number
print('GPA: ', gpa)

# Ask the user if they want to calculate their GPA again
run_again = input('Do you want to calculate your GPA again? (Yes/No): ').strip().lower()
if run_again != "yes":
print("See you again soon!")
break

