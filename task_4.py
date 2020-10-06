# Task 4

# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

# Remember the rules:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
choices_list = ["rock", "scissors", "paper"]
print("Welcome to Rock, Paper, Scissors \nChoose from the list \n{0}".format(choices_list))

player_1 = input('Enter player 1 name: ')
player_2 = input('Enter player 2 name: ')


def rps_game(choice_1, choice_2):
    if choice_1 == choice_2:
        print("It is a draw")
    
    elif choice_1 =='rock':
        if choice_2 == 'scissors':
            print('Player {0} wins \n'.format(player_1))
        else:
            print('Player {0} wins \n'.format(player_2))
    
    elif choice_1 == 'scissors':
        if choice_2 == 'paper':
            print('Player {0} wins \n'.format(player_1))
        else:
            print('Player {0} wins \n'.format(player_2))
    
    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            print('Player {0} wins \n'.format(player_1))
        else:
            print('Player {0} wins \n'.format(player_2))

while True:

    choice_1 = input('Player {0} turn, choose from the list: '.format(player_1)).lower()
    if (choice_1 not in choices_list):
        print('Please {0} enter options from the given list only \n'.format(player_1))
        continue

    choice_2 = input('Player {0} turn, choose from the list: '.format(player_2)).lower()
    if (choice_2 not in choices_list):
        print('Please {0} enter options from the given list only \n'.format(player_2))
        continue

    rps_game(choice_1, choice_2)

    play_again = input('Play again? Yes or No: ').lower()

    if play_again == 'no':
        break