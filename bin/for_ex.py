S = 'python'
for a in S:
    print('a = ', a, end=' ')
    print(id(a), end=' ')

b = 'java'
L = [10, 20, 30]
for b in L:
    print('b =', b)
print('Now a and b =', a, b)

D = {'A': 10, 'B': 20}
for K in D:
    print('K = ', K)
line = '-' * 40
print(line)
for K in D.keys():
    print('Key = ', K, 'Value = ', D[K])
print(line)
for V in D.values():
    print('V = ', V)
print(line)
# --------------------------------------------------------------------------------------------------------------------

for i in D.items():  # [('A', 10), ('B', 20)]
    print('i = ', i, i[0], i[1])
print(line)

# --------------------------------------------------------------------------------------------------------------------

for i, j in D.items():
    print(i, j)
print(line)

# ---------------------------------------------------------------------------------------------------------------------

hosts = ['h1', 'h2', 'h3']
ips = ['ip1', 'ip2']
Z = zip(hosts, ips)  # generator function.
print(Z)  # only shows the memory location of Z, because zip function does allow to show the value of object
print(list(Z))  # when referred to list it shows the values. But only the matched values.

for h, p in zip(hosts, ips):
    print(h, p)

# ---------------------------------------------------------------------------------------------------------------------
# for(i=2;i<10;i++)
r1 = range(10)
r2 = range(1, 10)
r3 = range(1, 10, 2)
print(list(r1), list(r2), list(r3), sep='\n')
r4 = range(10, 1, -1)
print(list(r4))

# ----------------------------------------------------------------------------------------------------------------------
for i in range(2, 10, 2):
    print('i = ', i)

# ----------------------------------------------------------------------------------------------------------------------

for h in range(0, len(hosts)):
    print(hosts[h])

for h in hosts[::2]:
    print('h =', h)
print(line)

# ----------------------------------------------------------------------------------------------------------------------

comp = ['IBM', 'DELL', 'SAP', 'DEL2']
for c in comp:
    if c.startswith('DEL'):
        print('Found')
        break
else:
    print('NF')

print(line)

# ----------------------------------------------------------------------------------------------------------------------

for i in comp:
    if not i.startswith('DEL'):
        continue
    if i.startswith('DEL'):
        print('some logic')
    print('last stmt of for')
