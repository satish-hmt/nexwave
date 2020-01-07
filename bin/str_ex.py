a = 'PERSON'
print(a)
b = "PERSON'S"
c = '''PERSON'S HEIGHT XYZ"''' #in python multiline comment is also stored as an object but when its reference count becomes
# zero so it goes to garbage and ignored but when it is refered to a variable its considered.
d = """PERSON"""
print(b,c,d,sep='\n')

s1 = 'Hello'
s2 = 'py'
s3 = s1 + s2
s4 = s1 * 10
print(s3, s4)
line = '_'*40
print(line)
e = 'PERSON\'S'
print(e)
f = 'c:\newfolder\test.py'
print(f)
f1 = r'c:\newfolder\test.py' #because on print f \n and \t acts as escape sequence.
print(f1)
g = 'WEL COME'
#    01234567  automatic index for the above string(WELL COME).
print(g)
print(len(g))
print(g[1])
print(g[1:6]) #to get substring/sclicing. here start index is inclusive and end index is excluded.
print(g[1:]) #prints till the end of the string.
print(g[:6])
print(g[:])
h = g[:]
print(id(h), id(g))
#--------------------------------------------------------------------------------------------------
#step
print(g[1:6:1])
print(g[1:6:2])
print(g[::-1]) #traversing in reverse.
print(g[::-2])
print(g[6:1:-2])

#-----------------------------------------------------------------------------------------------
#-ve index:
print(g[-7:-3])
print(g[len(g)-4:])#printing last 4 characters of the string.
print(g[-4:])#printing last 4 caracters.

#-----------------------------------------------------------------------------------------------
#str -> class
i = 10
j = str(i) #'10'
k = str('python')
print(i,j,k,sep='\n')
r1 = g.startswith('WEL')
print('r1 = ', r1)
r2 = g.endswith('OME')
print('r2 = ', r2)
r3 = g.isupper()
r4 = g.upper()
print(r3, r4, sep='\n')
r5 = g.islower()
r6 = g.lower()
print(r5, r6, sep='\n')
l='abc'
r7 = l.isalpha() #checking for alphabets.
m = '123'
r8 = m.isdigit() #checking for digits.
n = 'abc123'
r9 = n.isalnum() #checks for both alphabet and number, alphanum can be numbers or alphabets or both.
print(r7, r8, r8, sep = '\n')
r10 = n[-3].isdigit()
print(r10)
r11 = g.count('E')
print('e11 = ', r11)
r12 = g.index('E')
r13 = g.find('E')
print(r12,r13)
r14 = g.index('E',3)#this looks for e after 3rd index.
r15 = g.index('E',3,8)#this finds E between 3 and 5.
print(r14,r15)
r16 = g.rindex('E')#searches for E from the end.
print('r16 =', r16)
p=' wel come '
r17 = p.strip() #removes extra space from the ends but not in between.
r18 = p.lstrip()
r19 = p.rstrip()
print(r17, r18, r19, sep='\n')
q = '[wel[come][]'
r20 = q.strip(']w[e')#checks for all the characters till a mismatch and then searches from the
    #right end till a mismatch occurs.
r21 = q.lstrip('w[')
r22 = q.rstrip('][e')
print(r20,r21,r22, sep='\n')
r23 = g.replace('E','e')#can be done to a substring also.
print('r23 = ',r23)
r24 = g.split()#whereever there is a space the string splits and returns as a list.
r25 = g.split('E')#splits where E is present.
x=10
y=20
z=x+y
r26 = 'add ofx and y is z'
r27 = 'add of {} and {} is {}'.format(x,y,z)
r28 = 'add of {1} and {0} is {2}'.format(x,y,z)

#Python version > 3.5

r29 = f'add of {x} and {y} is {z}'

r30 = '-'.join(g)#join - sign between the characters of g.
r31 = 'xyz'.join(r24)
print(r24,r25,r26,r27,r28,r29,r30,r31,sep='\n')










