#filter
mylist=[1,2,3]
def multiplyby2(item):
	return item*2

def onlyodd(item):
	return item % 2 != 0

print(list(filter(onlyodd, mylist)))
print(mylist)