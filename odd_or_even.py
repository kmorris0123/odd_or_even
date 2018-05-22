playing = True

while playing == True:

	in_num = int(input("Input a number: "))

	if in_num % 2 == 0:
		print("The number is even!")
	elif in_num % 4 == 0:
		print("The number is a multiple of 4!")
	else:

		print("The number is odd!")

	play_again = input("Do you want to play again? Yes or No: ")

	if play_again == "yes":
		playing = True

	else:
		print("Thanks for playing!")
		playing = False


