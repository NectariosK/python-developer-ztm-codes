#Fibonacci
def fibonacci(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b 
		b = temp + b

for x in fibonacci(20):
	print(x)

#Solving the Fibonacci using a list
'''
def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(100))
'''