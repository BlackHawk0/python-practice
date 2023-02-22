import random

word_list = ['python', 'swift', 'ruby', 'javascript', 'computer', 'csharp']

def is_valid_input(user_input):
    if user_input.isalpha() and len(user_input) == 1:
        return True
    else:
        return False

def is_already_guessed(user_input, guessed_letters):
    if user_input in guessed_letters:
        return True
    else:
        return False

def is_game_over(dash_word, remaining_guesses):
    if remaining_guesses == 0:
        return True
    elif '-' not in dash_word:
        return True
    else:
        return False

def display_game(dash_word, remaining_guesses):
    print(' '.join(dash_word))
    print(f'You have {remaining_guesses} incorrect guesses remaining.')

def play_game():
    remaining_guesses = 6
    guessed_letters = []
    game_over = False
    secret_word = random.choice(word_list)
    print(secret_word)
    dash_word = list('-' * len(secret_word))

    print('Welcome to Hangman!')
    while not game_over:
        display_game(dash_word, remaining_guesses)
        user_input = input('Please guess a letter: ').lower()

        if not is_valid_input(user_input):
            print('Invalid input. Please enter a single letter.')
            continue
        elif is_already_guessed(user_input, guessed_letters):
            print('You have already guessed that letter. Please try another one.')
            continue
        else:
            guessed_letters.append(user_input)

        if user_input in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    dash_word[i] = user_input
        else:
            remaining_guesses -= 1

        if is_game_over(dash_word, remaining_guesses):
            game_over = True
            display_game(dash_word, remaining_guesses)
            if '-' not in dash_word:
                print('Congratulations! You win!')
            else:
                print(f'Sorry, you lost. The secret word was "{secret_word}".')
    
    play_again = input('Do you want to play again? (y/n)').lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing Hangman!")

play_game()
