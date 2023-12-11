import random
word_list = ['banana', 'apple', 'orange', 'grapes', 'dates']
print(word_list)


word = random.choice(word_list)
print(word)


guess = input('Enter letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Opps! Thats not a valid input')


