# Variable keyword only argument
def add(a, b=10, *c, d, e, **f):  # here f will take values for a dictionary.
    print('Extra kw only arg = ', f)  # f will return a dictionary.
    r = a + b + sum(c) + d + e + sum(f.values())
    return r


r1 = add(10, d=20, e=30)
print('r1 = ', r1)
print('-'*40)
r2 = add(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90)
print('r2 = ', r2)

D = {'d': 50, 'e': 60, 'x': 70}
r3 = add(10, 20, 30, 40, **D)  # d's and e's value will be assigned to d and e in the function and x will
# be the extra keyword only arguments
print('r3 = ', r3)



