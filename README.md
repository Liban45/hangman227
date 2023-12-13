# Hangman Game

## Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This project aims to create a simple command-line  version of the hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player tries to guess the word by suggesting letters. The player has a limited number of lives, and each incorrect guess results in the loss of a life. The game ends when the player correctly guesses the word or runs out of lives.

### Aim of the Project
This project aims to provide a basic implementation of the classic Hangman game. It is a beginner-friendly project to practice Python programming and learn basic game mechanics.

## What I Learned

### Stages of Development
The development of the Hangman Game involved several key stages:

1. **Function Definitions:** Started by defining functions for core game functionalities, such as selecting a random word, checking a guessed letter, and asking for input.

2. **Object-Oriented Programming (OOP):** Transitioned to an object-oriented approach by encapsulating the game logic into a `Hangman` class. This allowed for better organization of code, improved readability, and easier maintenance.

3. **Abstraction:** Leveraged abstraction to hide complex implementation details and provide a simplified interface for interacting with the game. This made the code more accessible, especially for those who may not be familiar with the internal workings of the game.

### Object-Oriented Programming
The project demonstrated the advantages of using object-oriented programming:

- **Encapsulation:** The `Hangman` class encapsulates the game's state and behavior, promoting a cleaner separation of concerns.
  
- **Inheritance:** While not explicitly showcased in this small project, OOP principles allow for easy extension of functionality in future iterations or variations of the game.

- **Code Reusability:** By encapsulating game logic within a class, the code becomes more modular and can be reused in other projects or extended for more features.

### Abstraction for Code Accessibility
Abstraction played a crucial role in making the code accessible:

- **Simplified Interface:** By exposing only essential functions and hiding internal complexities, abstraction provides a simplified interface for users of the code. For example, users interact with the `ask_for_input` method without needing to understand the intricacies of letter checking and state management.

- **Readability:** Abstraction enhances code readability by allowing developers to focus on high-level concepts and interactions rather than getting bogged down in implementation details. This is especially beneficial when collaborating with others or returning to the code after some time.

- **Ease of Maintenance:** With abstraction, modifications to the internal workings of the game can be made without affecting external code that relies on the provided interface. This reduces the risk of unintended side effects during maintenance or updates.

In summary, the project not only resulted in a functional Hangman game but also provided valuable insights into the benefits of OOP and abstraction in software development.


## Installation
1. Clone the repository to your local machine:
   git clone https://github.com/your-username/hangman227.git
2. Navigate to the project directory:
   cd hangman227
3. Run the game:
   python milestone_5.py

   
## Usage
1. The game will prompt you to guess a letter.
2. Enter a single alphabetical character as your guess.
3. Continue guessing until you correctly guess the word or run out of lives.


## File Structure
hangman227/</br>
|-- hangman</br>
&nbsp;  |-- hangman_Template.py</br>
&nbsp; |-- milestone_2.py</br>
&nbsp; |-- milestone_3.py</br>
&nbsp;  |-- milestone_4.py</br>
&nbsp;  |-- milestone_5.py</br>
|-- README.md</br>
|-- .gitignore



