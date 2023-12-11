import random
word_list = ['banana', 'apple', 'orange', 'grapes', 'dates']

secret_word = random.choice(word_list)
print(secret_word)


def check_guess(guess):
    guess.lower()
    if guess in secret_word:
        print(f'Good guess {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word')


def ask_for_input():

    while True:
        guess = input('Guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid input! Please enter a single alphabetical character.')
            continue
    check_guess(guess)

ask_for_input()