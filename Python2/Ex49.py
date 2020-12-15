mag_list = ['Micro','Micro','Very Minor','Minor','Light','Moderate','Strong','Major','Great']

while True:
    mag = input('please enter a magnitude ')
    try:
        # mag_r = mag rounded down
        mag_r = int(float(mag)//1)
        if mag_r < 0:
            print('please enter a valid input')

        elif 0 <= mag_r < 10:
            print(mag_list[mag_r])
            break

        elif mag_r >= 10:
            print('Meteoric')
            break

    except:
        print('please enter a valid input')

        
