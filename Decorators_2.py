#DECORATORS PATTERN
def my_decorator(func):
	def wrap_funct(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_funct

@my_decorator
def hello(greeting, emoji=':)'):
	print(greeting,emoji)

hello('Hi, there')