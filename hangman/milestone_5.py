def play_game(word_list):
  num_lives = 5
  game = Hangman(word_list, num_lives)
  while True:
    if num_lives == 0:
      print('You lost!')
    elif num_letters > 0:
      Hangman.ask_for_input()
    else:
      print('COngrats you won the game!')





import random
class Hangman:

  def __init__(self, word_list, num_lives = 5):
    self.num_lives = num_lives
    self.word_list = word_list
    self.word = self.secret_word()
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.list_of_guesses = []

  def secret_word(self):
    return random.choice(self.word_list)
  
  def __str__(self):
    return f'Your secret word is {self.secret_word()}'







  
  def check_guess(self, guess):
    guess.lower()
    if guess in self.word:
      print(f'Good guess {guess} is in the word')
      for letter in self.word:
        if letter == guess:
          self.word_guessed.replace(self.word_guessed[self.word.index(guess)], guess)
      self.num_letters -= 1
    else:
      print(f'Sorry, {guess} is not in the word')
      self.num_lives -= 1
      print(f'You have {self.num_lives} lives left.')
  




  def ask_for_input(self):
      while True:
        guess = input('Guess a letter: ')
        if len(guess) != 1 or (guess.isalpha()) == False:
          print('Invalid input! Please enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
          print('You already tried that letter!')
        else: 
          print('Well done')
      else:
        check_guess(guess)
        list_of_guesses.append(guess)




play_game(['banana', 'apple', 'orange', 'grapes', 'dates'])







    



