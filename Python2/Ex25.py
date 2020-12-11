time = int(input('please enter any number of seconds'))

days = time//(24*60*60)
time %= (24*60*60)
hours = time//(60*60)
time %= (60*60)
mins = time//60
time %= 60

print(f'{days}:{hours:0>2d}:{mins:0>2d}:{time:0>2d}')