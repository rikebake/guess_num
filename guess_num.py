import random 
guess = 0 # the #of guess
r = random.randint(1,100)
while True:
	user_guess = int(input('input a integer '))# the number that user guesses
	guess += 1#guess = guess + 1
	if user_guess == r:
		print('correct!','total ',guess,'times of guess')
		break
	elif user_guess > r:
		print('larger ')
	elif user_guess < r:
		print('smaller')
	print(guess,'times')

