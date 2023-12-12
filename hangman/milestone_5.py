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

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
        print('Current State:', ' '.join(self.word_guessed))
        print('--------------------------------------')

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
                break  
            

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            return game.word_guessed
        elif game.num_lives > 0 and game.num_letters > 0:
          game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congrats, you won the game!')
            return game.word_guessed
        

# Example usage:
play_game(['banana', 'apple', 'orange', 'grapes', 'dates'])




