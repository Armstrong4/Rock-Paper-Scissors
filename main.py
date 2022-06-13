import random

winner = ''

# Computer Choice.
game_options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(game_options)

# Getting User Choice.
user_choice = ''
while (user_choice != 'rock'
       and user_choice != 'scissors'
       and user_choice != 'paper'):
    user_choice = input('rock, paper or scissors? ')

# Game logic : Paper beats Rock, Rock beats Scissors and Scissors beats Paper
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')