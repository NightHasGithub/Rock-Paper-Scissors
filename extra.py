import random
import json
from os.path import exists

def getChoices():
	return ["rock", "paper", "scissors"]

def getRandomChoice():
	return random.choice(getChoices())

def createDataFile():
	out_file = open("data.json", "w")
	json.dump({
		"player": {
		"score": 0
		},
		"computer": {
		"score": 0
		},
	}, out_file, indent = 6)
	
	out_file.close()

def getPlayerScore():
	with open('data.json') as f:
  		data = json.load(f)
  		return data['player']['score']

def getComputerScore():
	with open('data.json') as f:
  		data = json.load(f)
  		return data['computer']['score']

def win():
	if not exists("data.json"):
		createDataFile()
	d = {
			"player": {
			"score": getPlayerScore() + 1
		},
			"computer": {
			"score": getComputerScore()
		},
	}
		
	with open('data.json', 'w') as json_file:
  		json.dump(d, json_file)

def loss():
	if not exists("data.json"):
		createDataFile()
	d = {
			"player": {
			"score": getPlayerScore()
		},
			"computer": {
			"score": getComputerScore() + 1
		},
	}
		
	with open('data.json', 'w') as json_file:
  		json.dump(d, json_file)