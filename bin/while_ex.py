a = 0
while a<10:
    print('a =', a)
    a = a + 1

S = 'python'
b = 0
while b<len(S):
    print('b =', S[b])
    b += 1

L = ['FN', 'LN', 'ADR', 'a1', 'FN', 'ADR', 'a2', 'FN']
i = 0
while i < len(L):
    if L[i] == 'ADR':
        i = i+1
        print(L[i])
        i = i+1
    else:
        i = i + 1

j = 0
while j < len(L):
    if L[j].startswith('a'):
        print('found')
        break
    else:
        j = j + 1
else:
    print('nf')

K = 0
while K < len(L):
    if not L[K].startswith('a'):
        K = K + 1
        continue
    print(L[K])
    K = K + 1
    print('Last stmt of while')


cart = []
while True:
    i = input('Enter Item:')
    cart.append(i)
    ch = input('Quit(Y/N)?: ')
    if ch == 'y':
        print('cart =', cart)
        break



