#List->Class
l1 = list([10,20,30])
#-ve index   -4  -3    -2         -1     
l2 =        [10,12.5,'python',['a','b']]
#index        0   1      2         3
print(l2)
print(l2[1])
print(l2[2][1])
print(l2[-1:1:-1])

#add to the list

l2.append(200)
print('append = ',l2)

l2.insert(2,300)#300 will be inserted at second position.
print('insert = ',l2)

l3 = [10,20]
l4 = ['a','b']
l5 = l3 + l4
l6 = l3 * 10
print(l5,l6,sep='\n')

l3.extend(l4)
print('Extend = ',l3)

#Remove

r1 = l5.pop()#element which is poped is stored in r1.
print('r1 = ', r1,l5)

r2 = l5.pop(2)#pop the element in 2nd index.
print('r2 = ', r2,l5)

r3 = l5.remove(20)#only the first occurence will be removed.
print('remove = ', r3, l5)

del l5[0]#deletes the element.
print('after del ', l5)

#Update

print('l3 = ', l3)

l3[1] = 'java'
print('after update = ',l3)

#Some other methods:

l6 = [10, 30, 20]
l6.sort() #ascending order. and will not work for hetrogenous data.
print('sort asc = ', l6)
l7 = ['z','a','b']
l7.sort(reverse = True)#desc
print('sort desc = ', l7)
l8 = [10,'a', 20, 'b']
l8.reverse()
print('reverse = ',l8)
l8.clear()#clears everything from l8.
print('l8 = ', l8)


#Copy:
l =[10, ['a','b']]
m=l3#reference copy.
n = l.copy() #shallow copy.
#copy module: ->copy(), deepcopy().
import copy
p = copy.deepcopy(l)
print(id(l[0]), id(p[0]))
print(id(l[1]), id(p[1]))






























