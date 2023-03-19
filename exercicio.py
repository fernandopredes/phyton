# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")

numbers = [1, 2, 4]
strange = [x+1 for x in numbers]
print(strange)

friends = ["Rolf", "Sandra", "Sam", "Carol"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)


def double(x):
    return x* 2

sequence = [1,3,5,9]
d = [double(x) for x in sequence]
print(d)

users = [
    (0, 'bob', 'password'),
    (1, 'lucas', 'bob123'),
    (2, 'jose', 'long4assword'),
    (3, 'username', '1234'),
]

username_mapping = {user[1]: user for user in users}



student = {'name': 'Jose', 'school':'Computing', 'grades': (66,77,88)}
print(sum(student['grades']))

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school':'Computing', 'grades': (66,77,88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count
