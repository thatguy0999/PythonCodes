while True:
    human_age = input('please enter a human age to be converted to dog years')
    try:    
        human_age = int(human_age)
        if human_age <= 0:
            print('please enter a valid input')

        elif human_age <= 2:
            print(f'that age in dog years is {human_age*10.5}')

        else:
            print(f'that age in dog years is {(human_age - 2)*4 + 21}')
        
    except:
        print('please enter a valid input')



