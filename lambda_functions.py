#lambda functions
from functools import reduce
mylist=[1,2,3]
'''
def multiplyby2(item):
	return item*2

def onlyodd(item):
	return item % 2 != 0

def accumulator(acc, item):
	print(acc, item)
	return acc + item
'''

#print(list(map(multiplyby2, mylist)))
#print(list(filter(onlyodd , mylist)))
#print(reduce(accumulator, mylist, 0))

#USING LAMBDA FUNTIONS
#print(list(map(lambda item: item*2, mylist)))
#print(list(filter(lambda item: item % 2 != 0, mylist)))
print(reduce(lambda acc, item: acc + item, mylist, 0)) #With or without 0 it works.
print(mylist)