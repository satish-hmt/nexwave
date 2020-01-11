def add():
    a = 10
    b = 20
    c = a + b
    #  return c  # after returning the value the function execution will stop.
    #  print('After Return')  # this print won't execute.
    #  return a, b, c  # will return a tuple of all the values.
    #  return [a, b, c]
    return (a+b)/(a-b)  # we can write one line expression for return.


add()

r1 = add()
print('r1 = ', r1)
