#map, filter,zip 
#MAP------>modified from 'pure_function.py'
mylist=[1,2,3]
def multiplyby2(item): #from list to item
	#newlist=[]
	#for item in list:
	#	newlist.append()
	return item*2
'''
print(map(multiplyby2, [1,2,3]))
Displays the mapping, in order to print the list, see below
'''
print(list(map(multiplyby2, mylist)))
print(mylist) #mylist did not get mopdified, this explains that the function above is a pure function