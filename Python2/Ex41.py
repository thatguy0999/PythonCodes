note, octave = input('please enter a note in a certain octave ')
octave = int(octave)

music = {
    'c':261.63,
    'd':293.66,
    'e':329.63,
    'f':349.23,
    'g':392.00,
    'a':440.00,
    'b':493.88,
}

print(f'the frequency is {music[note]/(2**(4-octave)):.2f}')