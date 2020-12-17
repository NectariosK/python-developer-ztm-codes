#Exercise on exteded list
class SuperList(list): #The power of python related to inheritance//list is a subclass  of the object 
	def __len__(self):
		return 1000

super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))