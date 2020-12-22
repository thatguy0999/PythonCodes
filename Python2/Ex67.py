total = 0

while True:
    age = input('please enter the age of the guest ')
    if age == '':
        break

    else:
        age = int(age)
        if age <= 2:
            pass

        elif 3 < age < 12:
            total += 14

        elif age >= 65:
            total += 18

        else:
            total += 23

print(f'the total cost of all the guests is ${total:.2f}')