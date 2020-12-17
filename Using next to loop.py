#More on using next to loop
def speacial_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			print(iterator)
			print(next(iterator)*2)
		except Stopiteration:
			break

speacial_for([1,2,3])