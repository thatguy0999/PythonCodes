events = {
    'January 1':'New Year\'s Day',
    'July 1':'Canada Day',
    'December 25':'Christmas Day',
}

while True:
    day = input('enter the date of a holiday ')
    try:
        print(f'the holiday on that day is {events[day]}')

    except:
        print('no known fixed-date holidays on that day')