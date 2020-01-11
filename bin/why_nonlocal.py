count = 0


def create_acc():
    global count
    count += 1


def delete_acc():
    global count
    count -= 1


create_acc()
delete_acc()
count = 100
delete_acc()
print('Total Accounts = ', count)


def acc():
    c = 0

    def ca():
        nonlocal c
        c = c + 1

    def da():
        nonlocal c
        c = c - 1

    def ta():
        print('total = ', c)

    return ca, da, ta

f1, f2, f3 = acc()  # acc() will return a tuple (ca, da ,ta) so by this statement f1, f2, f3 are assigned ca, da, ta.
f1()
f1()
c = 100  # this is a global variable which the function cannot access.
f2()
f3()
