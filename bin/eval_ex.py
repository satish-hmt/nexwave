a = '10'
b = int(a)
c = eval(a)
print(a, b, c)

# ---------------------------------------------------------------------------------------------------------------------
d = '[10, 20, 30]'
e = 'Hello'
f = list(e)
print(f)
g = list(d)
h = eval(d)  # accepts a string and considers what's inside the quotes as an expression.
print(g)
print(h)

i = 10
j = 20
k = eval('i+j')
print(k)
