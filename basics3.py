#EXERCISE TO CHECK FOR DUPLICATES
some_list=['c','o','i','t','u','s']
duplicates=[]
for item in some_list:
  if some_list.count(item)>1:
    if item not in duplicates:
     duplicates.append(item)    
        
print(duplicates)

#Functions
def myFunction(emoji, name):
  print(f'Helllooo {name}{emoji}')
  #print('The  is: {} and has the {}'.format('name','emoji'))

#position arguments
myFunction('😏','Nectar')

#keyword arguments
myFunction(name='Nectarios',emoji='😏')

#check highest & even number
def high(mylist):
  evens=[]
  for item in mylist:
    if item %2==0:
      evens.append(item)
  return max(evens)
print(high([51,58,5487,4598,526,325968,25,3164351]))

#Walrus operator usage
a='Oh hello there'

if((n:=len(a))>5):
  print(f'This text contains {n} characters')

while ((n:=len(a))>1):
  print(n)
  a = a[:-1]