#super & object introception
class User(object):
	def __init__(self, email):
		self.email=email
	def sign_in(self):
		print('logged in')

class Wizard(User):
	def __init__(self, name, power, email):
		super().__init__(email)
		self.name=name
		self.power=power

	def attack(self):
		print(f'Attacking with power of {self.power}.')
'''	
class Archer(User):
	def __init__(self, name, num_arrows):
		self.name=name
		self.num_arrows=num_arrows

	def attack(self):
		print(f'Attacking with arrows: arrows left {self.num_arrows}.')
'''
#introception
wizard1 = Wizard('Merlin', 16, 'merlin@gmail.com')
#print(wizard1.email)
print(dir(wizard1))
#archer1 = Archer('Robin', 34)
#wizard1.attack()
#archer1.attack()