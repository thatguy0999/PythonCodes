# letter = input('please enter a letter of the alphabet')

# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('that letter is a vowel')

# elif letter == 'y':
#     print('that letter can be either a vowel or consonant')

# else:
#     print('that letter is a consonant')

Vowel = {'a','e','i','o','u'}

letter = input('please enter a letter of the alphabet')

if letter in Vowel:
    print('that letter is a vowel')

elif letter == 'y':
    print('that letter can be either a vowel or consonant')

else: 
    print('that letter is a consonant')