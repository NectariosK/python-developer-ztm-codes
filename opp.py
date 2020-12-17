#OOP
class playercharacter:
	#Class object attribute
	membership=True
	def __init__(self,name,age):
		if (self.membership):
		 self.name=name #attriutes
		 self.age=age
	
	def shout(self):
		#print('run')
		print(f'My name is {self.name}.')

	def run(self, hello):
		#print('run')
		print(f'My name is {self.name}.')

player1=playercharacter('Nectar', 24)

#help(list)
print(player1.shout())
print(player1.run('hello'))