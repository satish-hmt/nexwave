# Keywords only args
def add(a, b, *c, d, e):
    r = a+b+sum(c)+d+e
    return r


res = add(10, 20, 30, 40, 50, e=60, d=70)  # because other than first 2 arguments will be taken by c so we can pass
# the arguments with their names


def telnet(*cmds, h=None, p=None):
    return 'Hello'


res2 = telnet()
res3 = telnet('dir')
print(res2, res3)
res4 = telnet('dir', p=1, h=2)
print(res4)
