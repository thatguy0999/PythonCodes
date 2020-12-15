month_30 = ['09','04','06','11']
month_31 = ['01','03','05','07','08','10']
leap_year = False

date = input('please enter a date ')

y, m, d = date.split('-')

if (int(y)%400 == 0) or (int(y)%400 != 0 and int(y)%100 != 0 and int(y)%4 == 0):
    leap_year = True

if (m == '02' and int(d) == 28 and not leap_year) or (m == '02' and int(d) == 29 and leap_year) or (m in month_30 and int(d) == 30) or (m in month_31 and int(d) == 31):
    print(f'the next day is {y}-{int(m)+1:0>2d}-01')

elif m == '02' and int(d) == 28 and leap_year:
    print(f'the next day is {y}-{m}-29')

elif m == '12' and int(d) == 31:
    print(f'the next day is {int(y)+1:0>2d}-01-01')

else:
    print(f'the next day is {y}-{m}-{int(d)+1:0>2d}')

