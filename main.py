#25000 words
import random

wins = 0
loses = 0

clear = "\n" * 100
man = ['_________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ ',
    '|__________'] #Array of 7

f = open('data.txt', 'r')
f_content = f.read()
f_contents = f_content.split(',')

while True:
    print(clear)
    print("WELCOME TO HANGMAN")
    print(f'Current Score {wins} wins and {loses} loses')
    print("Press enter to start a new game")
    start_trigger = input("")

    print("Starting Game")

    word_choice = random.choice(f_contents).lstrip()
    word_choice_length = len(word_choice)
    individual_letters = list(word_choice)
    current_score = []
    for x in range(word_choice_length):
        current_score.append('_')
    current_stage = 0
    print("Game Setup")
    print(clear)

    print("HOW TO PLAY")
    print("Guess a letter and then press the enter key")
    print("Please note all letters are lowercase")
    print("Press enter to start the game")
    start_trigger = input("")
    print(clear)

    game_in_progress = True
    guess_number = 0
    incorrect_guesses = 0
    incorrect_letters = []
    guessed_letters = []
    while game_in_progress == True:
        correct_go = False
        invalid_go = False
        print(f'Guess number: {guess_number}')
        print(current_score)
        print(f'Incorrect Letters {incorrect_letters}')
        for x in range(incorrect_guesses):
            print(man[x])
        print("Please input your guess")
        current_guess = input("")
        for x in range(len(guessed_letters)):
            if current_guess == guessed_letters[x]:
                print('You have already guessed this letter')
                print('Press enter to try again')
                start_trigger = input("")
                invalid_go = True
        guessed_letters.append(current_guess)
        if invalid_go == False:
            for x in range(word_choice_length):
                if current_guess == individual_letters[x]:
                    current_score[x] = current_guess
                    correct_go = True
            if correct_go == False:
                incorrect_guesses += 1
                incorrect_letters.append(current_guess)
        for x in range(word_choice_length):
            game_in_progress = False
            win = True
            if current_score[x] == '_':
                    game_in_progress = True
                    break
        if incorrect_guesses == 8:
            game_in_progress = False
            win = False
        guess_number += 1
        print(clear)
    if win == True:
        print("Congratulations you win")
        print(f'The word was {word_choice} and you got it in {guess_number} guesses')
        wins += 1
    else:
        for x in range(incorrect_guesses):
            print(man[x])
        print('Oh no you lost')
        print(f'The word was {word_choice}')
        loses += 1
    print('Press enter to continue')
    start_trigger = input("")