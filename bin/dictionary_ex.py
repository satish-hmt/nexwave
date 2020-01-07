#dict -> class

D = { 'course':'python', 'dur':10, 'loc':'Blr'}
print(D['course'])
# Unordered.


#add or update
D['course'] = ['c++','java']
print(D)

#Copy
E = D.copy()

#Remove
r1 = D.pop('course')
print('pop = ',r1,D)

del D['dur']
print('After Del =', D)

r2 = D.popitem()
print('r2 = ', r2, D)


#Other Methods

K = E.keys()
V = E.values()
i = E.items()
print(K,V,i,sep='\n')

