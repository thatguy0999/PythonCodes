salary = 2400

while True:
    rating = input('what is the rating of this employee ')
    try:
        rating = float(rating)
        if rating == 0:
            print('Unacceptable peformance')
            print('no raise given')
            break

        elif rating == 0.4:
            print('Acceptable peformance')
            print(f'Raise of ${salary*rating} (new pay - ${salary*(rating + 1)})')
            break

        elif rating >= 0.6:
            print('Meritorious peformance')
            print(f'Raise of ${rating*salary} (new pay - ${salary*(rating + 1)})')
            break

        else:
            print('invalid input')

    except:
        print('invalid input')


