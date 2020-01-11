import addmodule  # with this statement the whole addmodule file is executed. * addmodule file is in lib.
print(addmodule.msg)
print(addmodule.add(10, 20))
line = '-'*40
print(line)

# second way to set environmental variable
import sys
print(sys.path)

# sys.path.append(r'C:\Users\lab365\Desktop\satish_python\lib')
# import add module
# from here continue the code.


# another way of writing import statement using  alias:
# import addmodule as a
# print(a.msg)
# print(a.add(10, 20))
# print(line)

# another way: to import what required from the module
# from addmodule import msg, add
# print(msg)
# print(add(10, 20))
# print(line)

# another way: for each element of the module imported we can give alias:
# from addmodule import msg as m, add as a
# print(m)
# print(a(10, 20))
# print(line)

# another way:
# from addmodule import *
# print(msg)
# print(add(10, 20))

import Project.net.addmodule

print(Project.net.addmodule.msg)
print(line)

# ----------------------------------------------------------------------------------------------------------------------

from Project.net.addmodule import msg, add
print(msg)
print(line)

# ----------------------------------------------------------------------------------------------------------------------

