import random

choices = ["rock", "paper", "scissors"]

def getChoices():
	return random.choice(choices)

computer_choice = getChoices()
data = input("Please input either Rock, Paper or Scissors")
player_choice = data.lower()

if player_choice == "rock":
	if computer_choice == "rock":
		print("You and the Computer both chose Rock, leading to a draw")
	elif computer_choice == "paper":
		print("You'r Rock was covered by the Computer's Paper")
	elif computer_choice == "scissors":
		print("The Computer's Scissors was defeated by you'r Rock")
elif player_choice == "paper":
	if computer_choice == "rock":
		print("The Computer's Rock was no match for you'r Paper")
	elif computer_choice == "paper":
		print("You and the Computer both chose Paper, leading to a draw")
	elif computer_choice == "scissors":
		print("The Computer cut up your Paper into nothingness")
elif player_choice == "scissors":
	if computer_choice == "rock":
		print("You'r Scissors was no match for the Computer's Rock")
	elif computer_choice == "paper":
		print("The Computer's Paper was no match for you'r Scissors")
	elif computer_choice == "scissors":
		print("You and the Computer both chose Scissors, leading to a draw")
else:
	print("ERROR: Please select either Rock, Paper or Scissors")