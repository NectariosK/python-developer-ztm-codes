#binary
print(bin(40))
print(int('0b101000', 2))
#strings
long_string = '''
neogjehrh
geogeo
geigeg
egeg
gmkeg
'''
print(long_string)

#escape sequence
weather = "\tIt's \"kinda sunny\" today"
print(weather)

#formatted strings
name  = 'Nectarios'
age = 22
print('Hi '+ name +'. You are ' + str(age)+' years old')
print(f'Hi {name}. You\'re {age} years old.')#this was update in Python3
#In Python 2, the format(dot format) used is shown below.
print('Hi {}. You\'re {} years old.'.format('Nectarios','22'))

#strings
selfish='01234567'
        #01234567
#[start:stop:stepover]
print(selfish[::-3])

#Exerice_1
birth_year=input('What year were you born?\n')
#print(type(birth_year))
age = 2020 - int(birth_year)
print(f'You are {age}')
#Exercise2
user_name=input('What is your user name?\n')
password=input('What is your password?\n')

length_of_password=len(password)
secret_password='*'*len(password)
print(f'{user_name}, your password is {secret_password} and it is {length_of_password} characters long.')
#list patterns
sentence=' '
new_sentence=sentence.join(['Hi','my','name','is','Nectarios.'])
print(new_sentence)
#dictionary
dictionary={
  'a':[1,2,3,4,5,6],
  'b':2,
  'c':3
}
print(dictionary['a'])
my_list=[{
  'a':[1,3,6,8,9],
  'b':2,
  'c':True
},
{
  'a':[1,2,3,4,5,6],
  'b':2,
  'c': True
}]
print(my_list[0]['a'][4])
print(dictionary['a'][2])
#dictionary_further_used
user={
  'basket':[1,2,3],
  'greet':'hello',
  'age':25
}
#user2=user.copy()
#print(user)
print(user.pop('age'))