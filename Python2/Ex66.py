total = 0
re = 0

grading = {
    'A+':4.0,
    'A':4.0,
    'A-':3.7,
    'B+':3.3,
    'B':3.0,
    'B-':2.7,
    'C+':2.3,
    'C':2.0,
    'C-':1.7,
    'D+':1.3,
    'D':1.0,
    'F':0.0,
}

while True:
    grade = input('please enter a grade ')
    if grade == '':
        break

    else:
        total += grading[grade]
        re += 1

print(f'the average points awarded are {total/re}')