days_28_29 = ['february']
days_30 = ['september','april','june','november']
days_31 = ['january','march','may','july','august','october','december']

while True:
    month = input('please state a month ')
    if month in days_28_29:
        print('there are 28 days normally but 29 in a leap year for that month')
        break

    elif month in days_30:
        print('there are 30 days for that month')
        break

    elif month in days_31:
        print('there are 31 days for that month')
        break

    else:
        print('please enter a valid input')