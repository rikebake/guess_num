import random 
while True: # to avoid upper < lower
	upper_rand = int(input('input the upper limit of the random number '))
	lower_rand = int(input('input the lower limit of the random number '))
	if upper_rand > lower_rand:
		break
	else:
		print('upper must larger than lower')

guess = 0 # the #of guess
r = random.randint(lower_rand,upper_rand)
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

