############### Day 5: Extra Challenges: Tuple of Student Sex################

# You work for a school and your boos wants to know how many female and male students are enrolled in the school. The school has saved the students in a list. Your task is to write a code that will count how many males and females in the list. Here is a list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# You code should return a list of tuples. The should return:
# [('Male',7), ()'female',6)]

def student_sex(students):
    maleC = 0
    femaleC = 0

    for student in students:
        if student.islower() == 'female':
            femaleC += 1
        elif student.islower() == 'male':
            maleC += 1

    ourTuple = [('Male', maleC), ('female', femaleC)]

    return ourTuple


print(student_sex(students))