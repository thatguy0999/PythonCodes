values = {
    'January':0,
    'February':31,
    'March':59,
    'April':90,
    'May':120,
    'June':151,
    'July':181,
    'August':212,
    'September':243,
    'October':273,
    'November':304,
    'December':334,
}

month = input('please enter the month you were born')
day = int(input('please enter the day of that month you were born'))
month = month.capitalize()

#cd stands for cumulative days (passed in a year)
cd = values[month] + day 

if cd >= 356 or 1 <= cd <= 19:
    print('Capricorn')

elif 20 <= cd <= 49:
    print('Aquarius')

elif 50 <= cd <= 79:
    print('Pisces')

elif 80 <= cd <= 109:
    print('Aries')

elif 110 <= cd <= 140:
    print('Taurus')

elif 141 <= cd <= 171:
    print('Gemini')

elif 172 <= cd <= 203:
    print('Cancer')

elif 204 <= cd <= 234:
    print('Leo')

elif 235 <= cd <= 265:
    print('Virgo')

elif 266 <= cd <= 295:
    print('Libra')
    
elif 296 <= cd <= 325:
    print('Scorpio')

elif 326 <= cd <= 355:
    print('Sagittarius')

