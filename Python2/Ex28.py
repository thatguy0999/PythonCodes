temp = int(input('what is the temperature of the air'))
wind = float(input('what is the wind speed'))

wci = 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)
print(f'{wci:.3f}')