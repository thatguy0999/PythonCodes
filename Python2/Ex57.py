year = int(input('please input a year'))

if year%400 == 0:
    print('it is a leap year')

elif year%400 != 0 and year%100 == 0:
    print('it is not a leap year')

elif year%400 != 0 and year%100 != 0 and year%4 == 0:
    print('it is a leap year')

else:
    print('it is not a leap year')