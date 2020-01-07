#Core data types.
#Numbers.(storing numbers).
#Collection of Characters(Strings).
'''
List
Tuple
'''
"""
Dictionary
Set
"""
'''
immutable types:
numbers
string
tuple
'''
'''
mutable types:
list
dictionary
set
'''

#Numbers:
a=10 #int
b=12.5 #float
c=0x12 #hex
d=0b1010 #bin
e=0o12 #oct
print('Hello')
print('a')
print('result = ',a,b,c,d,e,sep='|',end='.')#
print('test')#file=,flush=
f=int(20)
print(f)
print(a)
print(id(a)) #prints the refrence id.
print(type(a)) #prints the type of object its holding.
print(type(a).__name__) #to access only the name of the type.
a = 100 #the variable is assigned to new object. reference count of 100 is 1.
print(id(a))
b=a #reference copy.(a and b refering to same object i.e 100. reference count of 100 is 2
a=200 #now a no longer refering to object 100 but to 200. reference count of 100 is 1 and 200 is 1
b=300 #now b refers to 300 #reference count of 200 is 1 and 100 is 0 and 300 is 1.
#sys.getrefcount

