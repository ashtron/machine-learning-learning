# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

from random import randrange

running = True

def calculate_winner(player1_move, player2_move):
  player1_wins = None

  if player1_move < player2_move:
    if -(player1_move == 0 and player2_move == 2):
      player1_wins = True
    else:
      player1_wins = False
  elif player1_move > player2_move:
    if -(player2_move == 0 and player1_move == 2):
      player1_wins = False
    else:
      player1_wins = True

  return player1_wins

def play():
  computer_move = randrange(3)
  player_move = int(input("\nMake your move (0: rock, 1: paper, 2: scissors): "))
  num_move_map = { 0: "rock", 1: "paper", 2: "scissors" }

  print(f"\nYou played {num_move_map[player_move]}.")
  print(f"The computer plays {num_move_map[computer_move]}.")

  computer_wins = calculate_winner(computer_move, player_move)

  if computer_wins == True:
    print("\nThe computer wins!")
  elif computer_wins == False:
    print("\nYou win!")
  else:
    print("\nIt's a tie!")

while running:
  play()

  play_again = input("\nWould you like to play again? (y/n): ")

  if play_again == "n":
    print("\nGoodbye!")
    running = False
