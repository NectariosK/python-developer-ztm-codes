#Files with IO error
try:
	with open('app\sad.txt', mode='r') as my_file:
	#print(my_file.readlines())
		text = my_file.read() #change this to a read or write whenever required
		print(text)
except FileNotFoundError:
	print('File does not exist.')
	raise err
except IOError as err:
	print('IO error')
	raise err