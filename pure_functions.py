#pure_functions
#The class below was just added

Wizard={
	'name': 'Merlin',
	'power': 600
}

#newlist=[] #this could be here but this makes it located in the outside world of the function below
def multiplyby2(list):
	newlist=[]
	for item in list:
		newlist.append(item*2)
	return newlist

print(multiplyby2([1,2,3]))