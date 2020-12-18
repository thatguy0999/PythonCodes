total_sum = 0
total_re = 0

while True:
    no = float(input('please enter a number  '))
    if no == 0:
        break

    else:
        total_sum += no
        total_re += 1
    
print(f'the average is {total_sum/total_re:.3f}')