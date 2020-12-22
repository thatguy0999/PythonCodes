word = input('please enter a word  ')
new_word = ''

word = word.replace(' ','')
for i in range(len(word)):
    new_word += word[-(i+1)]

if new_word == word:
    print('palindrome')

else:
    print('not a palindrome')


