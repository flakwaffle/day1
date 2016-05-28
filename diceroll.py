import random



print("Welcome to the dice game!")
print("Press 'R' to roll the die!")
print("Enter 'exit' to exit the game!")

def game():
	while True:
		diceroll = random.randint(1, 6)
		confirm = input("> ")
		if confirm.lower() == "r":
			print("The dice has spoken! It rolled a {}.".format(diceroll))
			continue
		elif confirm.lower() == "exit":
			print("Goodbye!")
			break
		else:
			print("I'm sorry, please enter the correct input.")
			continue
		
	
game()


	
	