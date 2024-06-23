import random

def number_guessing_game():
	print("Welcome to the Number Guessing Game!")
	print("I have selected a number between 1 and 100. Can you guess it?")
	#Generate a random number
	number_to_guess = random.randint(1, 100)
	attempts = 0
	while True:
		try:
			guess = int(input("Enter your guess: "))
			attempts += 1
			if guess == number_to_guess:
				print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
				break
			elif guess < number_to_guess:
				print("Too low! Try again.")
			else:
				print("Too high! Try again.")
		except ValueError:
			print("Invalid input. Please enter a valid number.")

#Run the game
number_guessing_game()