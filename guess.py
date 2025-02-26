import random

r = random.randint (1,100)

while True:
	num = input ('Please input a number between 1 and 100: ')
	num = int(num)

	if num == r:
		print('You have guessed correctly!')
		break

	elif num < r:
		print('Your guess is smaller than the true number.')

	else:
		print('Your guess is larger than the true number')

