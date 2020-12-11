pressure = float(input('please input the pressure'))
volume = float(input('please input the volume (litres)'))
temperature = int(input('please input the temperature (kelvins)'))

print(f'the number of moles in the gas is {(pressure*volume)/(8.314*temperature)}')