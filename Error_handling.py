#Error handling 
#Using try, except and else (in that order)

while True:
	try:
		age = int(input('What is your age?'))
		print(age)
	except:
		print('Please enter a number.')
	else:
		print('Thank you!')
		break