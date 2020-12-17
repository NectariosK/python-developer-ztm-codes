#polymorphism
class User():
	def sign_in(self):
		print('logged in')

	def attack(self): #addig this because of line 15 (User.attack(self))
		print('Do nothing.')

class Wizard(User):
	def __init__(self, name, power):
		self.name=name
		self.power=power

	def attack(self):
		User.attack(self)
		print(f'Attacking with power of {self.power}.')
	
class Archer(User):
	def __init__(self, name, num_arrows):
		self.name=name
		self.num_arrows=num_arrows

	def attack(self):
		print(f'Attacking with arrows: arrows left {self.num_arrows}.')

wizard1 = Wizard('Merlin', 16)
archer1 = Archer('Robin', 34)

#print(wizard1.sign_in())
#wizard1.attack()
#archer1.attack()
print(wizard1.attack())

'''
#1st demostration
def player_attack(char):
	char.attack()

player_attack(wizard1)
player_attack(archer1)
'''
'''
#2d way
for char in [wizard1, archer1]:
	char.attack()
'''

#To have both User() and Wizard() or Archer() do to do the attack we ca do as follows:
