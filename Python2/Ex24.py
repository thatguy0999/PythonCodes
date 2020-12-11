days = int(input('please enter the number of days'))
hours = int(input('please enter the number of hours'))
mins = int(input('please enter the number of minutes'))
secs = int(input('please enter the number of seconds'))

time = days*24*60*60 + hours*60*60 + mins*60 + secs

print(f'the total length of time is {time} seconds')