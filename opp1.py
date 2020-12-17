#opp_first code
class player:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def run(self):
		print('run')

player1=player('Sophie', 24)

print(player1.name)
print(player1.age)