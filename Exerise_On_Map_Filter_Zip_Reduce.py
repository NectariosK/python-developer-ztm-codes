#ExeriseOnMapFilterZipReduce
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalized(string):
	return string.capitalize() #or upper()

print(list(map(capitalized, my_pets))) #NB:print(list(map(my_pets, capitalized))) DOESN'T WORK!!!
#print(my_pets.capitalized())----->Mistake

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def OverFifty(item):
	return item > 50

print(list(filter(OverFifty, scores))) #Remember this does't work if it is: print(list(filter(scores, OverFifty)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
	print(acc, item) #(73, 20) (93,65) ()
	return acc + item

print(reduce(accumulator, (scores + my_numbers)))