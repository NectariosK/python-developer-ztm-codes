#tuple data type
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(5 in my_tuple)
user = {
    (1, 2): [1, 2, 3, 4, 5, 6, 7],
    'greet': 'hello',
    'age': 25,
}
print(user['greet'])
#print(user'greet')
print(len(user))
print(len(my_tuple))

#set data type
my_set = {1, 2, 3, 4, 5}
your_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#difference
#print(my_set.difference(your_set))
#print(my_set)
#print(my_set.difference_update(your_set))
#print(my_set)#difference update

#intersection
print(my_set.intersection(your_set))
print(my_set & (your_set))
#union
print(my_set | (your_set))
#difference
print(my_set.difference(your_set))
#issubset
print(my_set.issubset(your_set))
#isuperset
print(your_set.issuperset(my_set))
#disjoint
print(my_set.isdisjoint(your_set))

#conditional logics
is_old = False
is_licenced = True
if is_old and is_licenced:
    print('You are old and licenced to drive!')

elif is_licenced:
    print('You are licenced.')
else:
    print('You are not of age.')

print('****')

#Ternary operator
#condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

#exercise to count and add up stuff in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)
print('**************\n')
#another loop with range
for _ in range(1):
    print(list(range(10, 0, -1)))
print('**************\n')
#enumerate
for i, char in enumerate('Hellooooo'):
    print(i, char)
print('**************\n')
for i, char in enumerate([1, 2, 3]):
    print(i, char)
print('**************\n')
for i, char in enumerate(list(range(100))):
    #print(i,char)
    if char == 50:
        print(f'Index of 50 is: {i}.')
########EXERCISE######
word = [
  [1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1],
  [1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
  [1,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0],
  [1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0],
  [1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
  [1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1]]
for row in word:
  for pixel in row:
    if (pixel==1):
      print('*', end='')
    else:
      print(' ', end='')
  print('')
 