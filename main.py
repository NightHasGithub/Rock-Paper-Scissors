import random
import time
import extra
import json

player_choice = input("Please input either Rock, Paper or Scissors").lower()

def startGame():
	print("Computer is choosing...")
	computer_choice = extra.getRandomChoice()
	time.sleep(1.5)
	match player_choice:
		case "rock":
			match computer_choice:
				case "rock":
					print("You and the Computer both chose Rock, leading to a draw")
				case "paper":
					print("You'r Rock was covered by the Computer's Paper")
					extra.loss()
				case "scissors":
					print("The Computer's Scissors was defeated by you'r Rock")
					extra.win()
		case "paper":
			match computer_choice:
				case "rock":
					print("The Computer's Rock was no match for you'r Paper")
					extra.win()
				case "paper":
					print("You and the Computer both chose Paper, leading to a draw")
				case "scissors":
					print("The Computer cut up your Paper into nothingness")
					extra.loss()
		case "scissors":
			match computer_choice:
				case "rock":
					print("You'r Scissors was no match for the Computer's Rock")
					extra.loss()
				case "paper":
					print("The Computer's Paper was no match for you'r Scissors")
					extra.win()
				case "scissors":
					print("You and the Computer both chose Scissors, leading to a draw")
		case _:
			print("[ERROR] Invalid type selected, choose between Rock, Paper or Scissors!")
startGame()