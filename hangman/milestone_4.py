class Hangman:
    import random
    word_list = ['banana', 'apple', 'orange', 'grapes', 'dates']
    word = random.choice(word_list)
    list_of_guesses = []


    def __init__(self, world_list, word, word_guessed, num_letters, list_of_guesses, num_lives=5):
        self.world_list = world_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
    

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f'Good guess {guess} is in the word')
        else:
            print(f'Sorry, {guess} is not in the word')

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if len(guess) != 1 or guess.isalpha():
                print('Invalid input! Please enter a single alphabetical character.')
                continue
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
    ask_for_input()






    



