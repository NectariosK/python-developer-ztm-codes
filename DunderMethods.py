#DunderMethods like __str__
class Toy():
    def __init__(self, color, size):
       self.color=color
       self.size=size
       self.my_dict = {
	       'name':'Yoyo',
	       'has_pets' : False
	       }

    def __str__(self):
       return f'{self.color}'

    def __len__(self):
       return 5

    def __call__(self):
       return('yess!')

    def __getitem__(self, i):
       return self.my_dict[i]

action_figure=Toy('Black', 4)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
#del action_figure