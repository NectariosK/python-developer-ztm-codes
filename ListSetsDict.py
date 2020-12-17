#ListSetsDict

#Lists
my_list1 = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 ==0]

print(my_list1)
print('\t')
print(my_list2)
print('\t')
print(my_list3)
print('\t')
print(my_list4)

#Sets---->Remember sets only allow unique items and no dupliates.
my_list1 = {char for char in 'hello'}
my_list2 = {num for num in range(0,100)}
my_list3 = {num**2 for num in range(0,100)}
my_list4 = {num**2 for num in range(0,100) if num % 2 ==0}

print(my_list1)
print('\t')
print(my_list2)
print('\t')
print(my_list3)
print('\t')
print(my_list4)

#Dict
simple_dict = {
	'a' : 1,
	'b' : 2,
	'c' : 3
}
my_dict = {key:value**2 for key,value in simple_dict.items()} 
#my_dict = {k:va**2 for k,v in simple_dict.items() for v%2==0}#---->with if statement

print(my_dict)