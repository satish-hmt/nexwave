a = 10
if a == 10:
    print('a eq 10')
if a > 10:
    print('a gt 10')
if a < 10:
    print('a lt 10')
'''
Else If.
'''
a = 10
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
elif a < 10:
    print('a lt 10')

'''
Else If Else
'''
a = 10
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
else:
    print('a lt 10')

S = 'python'
if 'th' in S:
    print('Substring Found.')

if not S.startswith('java'):
    print('Not java')

if S != 'c++':
    print('Not c++')

if S[1:3] == 'yt':
    print('yt found')

L1 = [10, 20]
L2 = L1
L3 = L1.copy()
if 20 in L1:
    print('20 found')

if L1 is L2:
    print('Both Refers same obj')

if id(L1) == id(L2):
    print('Both refers to same obj.')

if L1 == L2:
    print('Contents are same.')

if id(L1) == id(L3):
    print('Objects  same.')
else:
    print('Objects not same.')

D = {'A': 10, 'B': 20}
if 'B' in D:
    print('Key B found')

if 'B' in D.keys():
    print('Key B found')

if 20 in D.values():
    print('20 Found')

if ('A', 10) in D.items():
    print('items found.')

b = 10
c = 20
if b == 10 and c == 20:
    print('yes')

if a == 10:
    pass
