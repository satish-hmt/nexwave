x = 10  # Global


def f1():
    x=20

    def f2():
        y=30  # local scope. in this line a new x variable is created
        # now to change the value of x in f1 we use nonlocal.

        nonlocal x
        x = 200  # here the x referes to the x in f1

        print('F2 =', y)
    f2()  # we cannot call f2 function outside f1 function. we can access f2 only by returning it as
    # functions are also objects
    print('F1 = ', x)


f1()
print('Global = ', x)

print(dir(__builtins__))
f = open('abc.txt', 'w')

f.writelines(i+'\n' for i in dir(__builtins__))
f.close()

