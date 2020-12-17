#Regular expressions
#re
'''
import re

string = 'Search this inside of this text please!'

#print(re.search('this', string))
a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())
'''

#Using pattern
import re

pattern = re.compile('this')
string = 'Search this inside of this text please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string) #would work if the string in line 19 is the same as that in line 20
#print(a.group())
d = pattern.match(string)
print(c)