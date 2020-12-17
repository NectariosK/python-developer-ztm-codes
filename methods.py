#class methods ad static methods
#OPP
class PlayerCharacter:
	membership = True #Class object attribute
	def __init__(self, name, age):
		self._name=name #Attriburtes
		self._age=age #private

	def run(self):
		print('run')

	def speak(self):
		print(f'My name is {self._name} and I am {self._age} years old.')

'''
	@classmethod
	def adding_things(cls, num1, num2):
		return cls('Teddy', num1 + num2)

	@staticmethod
	def adding_things(num1, num2):
		return num1 + num2
'''
player1=PlayerCharacter('Tom', 39)
#player2=PlayerCharacter.adding_things(2,3)
print(player1.speak())