import random
import sys

play = ["rock", "paper", "scissors"]

computer = ""
player = ""

print("Welcome to the game of Rock, Paper, Scissors! Type \"exit\" to quit.")

computer = random.choice(play)
player = input("Rock, Paper, or Scissors?\n\n")

if player.lower() == "exit":
    sys.exit()
elif player.lower() == computer:
    print("Computer plays:", computer)
    print("Tie!")
elif player.lower() == "rock": # rock beats scissors, paper covers rock
    if computer == "scissors":
        print("You win!", player, "beats", computer)
    else:
        print("You lose!", computer, "covers", player)
elif player.lower() == "paper": # paper covers rock, scissors beats paper
    if computer == "rock":
        print("You win!", player, "covers", computer)
    else:
        print("You lose!", computer, "cut", player)
elif player.lower() == "scissors": # scissors beats paper, rock beats scissors
    if computer == "paper":
        print("You win!", player, "cut", computer)
    else:
        print("You lose!", computer, "beats", player)
else:
    print("That's not how to play the game...")
