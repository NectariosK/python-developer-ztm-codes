#Exercise_on_lambda_expessions

#SQUARE
mylist = [5, 4, 2]

newlist = list(map(lambda num: num**2, mylist))
print(newlist)

#LIST SORTING FROM 2ND NO.
a = [(5,6), (7,8), (10,-4), (52,53), (9,8)]
a.sort(key=lambda i: i[1]) #key is very important
print(a)