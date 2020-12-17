#GENERATORS
def my_generator_function(num):
	for i in range(num):
		yield i

for item in my_generator_function(1000):
	print(item)
