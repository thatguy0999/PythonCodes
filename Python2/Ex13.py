while True:
    change = input('how much change in cents')
    try:
        change = int(change)
        if change >= 0: 
            break
        elif change < 0:
            print('invalid input')
    except:
        print('invalid input')

dollar = change//100
change %= 100
fifty = change//50
change %= 50
twenty = change//20
change %= 20
ten = change//10
change %= 10
five = change//5
one = change%5

if change == 0: 
    print('You have paid exact amount')

else:
    print('Your change is')
    if dollar > 0:
        print(f'{dollar} one dollar coin(s)')
    if fifty > 0:
        print(f'{fifty} fifty cent coin(s)')
    if twenty > 0:
        print(f'{twenty} twenty cent coin(s)')
    if ten > 0:
        print(f'{ten} ten cent coin(s)')
    if five > 0:
        print(f'{five} five cent coin(s)')
    if one > 0:
        print(f'{one} one cent coin(s)')