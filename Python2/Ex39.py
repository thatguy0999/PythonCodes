sound_level = int(input('please enter a sound level in decibels'))

if sound_level < 40:
    print('more quiet than a quiet room')

elif sound_level == 40:
    print('as loud as a quiet room')

elif 40 < sound_level < 70:
    print('louder than a quiet room, more quiet than an alarm clock')

elif sound_level == 70:
    print('as loud as an alarm clock')

elif 70 < sound_level < 106:
    print('louder than an alarm clock, more quiet than a gas lawnmower')

elif sound_level == 106:
    print('as loud as a gas lawnmower')

elif 106 < sound_level < 130:
    print('louder than an a gas lawnmower, more quiet than a jackhammer')

elif sound_level == 130:
    print('as loud as a jackhammer')

else:
    print('louder than a jackhammer')