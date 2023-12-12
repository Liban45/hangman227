import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = self.secret_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def secret_word(self):
        return random.choice(self.word_list)

    def __str__(self):
        return f'Your secret word is {self.word}'

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess {guess} is in the word')
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid input! Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                if self.num_lives == 0 or self.num_letters == 0:
                    break  # Exit the loop if the game is over
        return self.word_guessed

# Example usage:
test1 = Hangman(['banana', 'apple', 'orange', 'grapes', 'dates'])
print(test1.ask_for_input())

    



