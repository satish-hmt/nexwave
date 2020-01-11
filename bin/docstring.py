L = []
print(dir(L))
print(help(L.pop))

import sys
print(help(sys))
'''
import addmodule
print(help(addmodule))  # first multiline comment of the module will be displayed!
'''
def add():
    '''
    Desc about add
    called-doc string
    '''
    # abc
    '''
    aaa aaa aaa
    '''


print(help(add))
