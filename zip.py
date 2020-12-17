#zip--->VERY IMPORTANT IN PYTHON
mylist=[1,2,3]
yourlist=[12,34,45]
theirlist=[20,50,60]

def multiplyby2(item):
	return item*2

def onlyodd(item):
	return item % 2 != 0

print(list(zip(mylist, yourlist,theirlist)))
print(mylist)