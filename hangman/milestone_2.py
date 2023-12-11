import random
word_list = ['banana', 'apple', 'orange', 'grapes', 'dates']
print(word_list)


word = random.choice(word_list)
print(word)


user_guess = input('Enter letter: ')

if len(user_guess) == 1 and user_guess.isalpha():
    print('Good guess!')
else:
    print('Opps! Thats not a valid input')


