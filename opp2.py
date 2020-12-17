#exercise
#Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


Gang=Cat('Gang', 12)
Ge=Cat('Ge', 2)
Geep=Cat('Geep', 10)

	
def ToFindOldestCat(*args):
	return max(args)       	
		

print(f'The oldest cat is {ToFindOldestCat(Gang.age, Ge.age, Geep.age)} years old.')