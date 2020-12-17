#reduce
from functools import reduce
mylist=[1,2,3]
'''
def multiplyby2(item):
	return item*2

def onlyodd(item):
	return item % 2 != 0
'''
def accumulator(acc, item):
	print(acc, item)
	return acc + item

print(reduce(accumulator, mylist, 0))
print(mylist)