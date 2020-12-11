winter = ['January','February']
spring = ['April','May',]
summer = ['July','August']
fall = ['October','November']

month = input('please enter a month ')
day = int(input('please enter a day of that month '))

month = month.capitalize()

if month in winter:
    print('winter')

elif month in spring:
    print('spring')

elif month in summer:
    print('summer')

elif month in fall:
    print('fall')

else:
    if month == 'March':
        if day < 20:
            print('winter')

        else:
            print('spring')

    elif month == 'June':
        if day < 21:
            print('spring')
        
        else: 
            print('summer')

    elif month == 'September':
        if day < 22: 
            print('summer')

        else:
            print('fall')

    else:
        if day < 21:
            print('fall')
        
        else:
            print('winter')