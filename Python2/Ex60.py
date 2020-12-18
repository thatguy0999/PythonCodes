from random import randint 

red_space = [1,3.5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

no = randint(0,38)
if no == 38:
    no = '00'

print(f'The spin resulted in {no}')
print(f'Pay {no}')

if no != '00' and no != 0:
    if no in red_space:
        hue = 'red'

    else:
        hue = 'black'

    print(f'Pay {hue}')
    if no%2 == 0:
        print(f'Pay Even')

    else:
        print(f'Pay Odd')
    
    if 1 <= no <= 18:
        print(f'Pay 1 to 18')

    else:
        print(f'Pay 19 to 36')

