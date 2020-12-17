#Debugging
#Linting-the use of pylint helps to see errors before we even run our code 
#use Ide/editor
#learn to read errors
#pdb-python debugger
#How pdb is used (below)

import pdb
def add(num1, num2):
	pdb.set_trace()
	return num1 + num2

add(4, 'svsvsdbd')
