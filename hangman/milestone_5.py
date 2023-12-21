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
            print(f'You lost! The word was: {game.word}')
            return game.word_guessed
        elif game.num_lives > 0 and game.num_letters > 0:
          game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congrats, you won the game!')
            return game.word_guessed
        
# Example usage:
play_game(['banana', 'apple', 'orange', 'grapes', 'dates', 
          'chicken', 'dog', 'cat', 'mouse', 'frog', 'abruptly', 'absurd',
          'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure',
          'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini',
          'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful',
          'buckaroo',  'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing',
          'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt',
          'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying',
          'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae',
          'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack',
          'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled',
          'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo',
          'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic',
          'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic',
          'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice',
          'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw',
          'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial',
          'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole',
          'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz',
          'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph',
          'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic',
          'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull',
          'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pyjama', 'peekaboo',
          'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw',
          'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips',
          'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb',
          'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy',
          'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths',
          'stretch', 'stronghold', 'stymied', 'subway', 'swivel',
          'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript',
          'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths',
          'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen',
          'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz',
          'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey',
          'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy',
          'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked',
          'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch',
          'zipper', 'zodiac', 'zombie'])




