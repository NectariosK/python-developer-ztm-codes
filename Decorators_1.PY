#DECORATORS USING HIGHER ORDER FUNCTIONS
def my_decorator(func):
	def wrap_funct():
		print('*******')
		func()
		print('*******')
	return wrap_funct

@my_decorator
def hello():
	print('Oh, hello there!')

@my_decorator
def bye():
	print('See you later.')

hello()
bye()
#hello2 = my_decorator(hello) #This is basically what the @my_decorator function does
#hello2() #Calling hello2