import random 

r = random.randint(1,100)
while True:
	user_guess = int(input('input a integer '))# the number that user guesses
	if user_guess == r:
		print('correct!')
		break
	elif user_guess > r:
		print('larger ')
	elif user_guess < r:
		print('smaller')

