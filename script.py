#read, write and append with files
#append (mode='a')
#write (mode='r')
#read and write(mode='r+')

with open('sad.txt', mode='r+') as my_file:
	#print(my_file.readlines())
	text = my_file.write(':(')
	print(text)