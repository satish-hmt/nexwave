F1 = open('out1.txt', 'w')
# for 'w' mode if there is no existing file then a new file is created.
# if there exists a file the evrything will be erased.

X = 10
S = 'python\n'
A = 'satish\n'
# writing the above two to a file
# for writing we have two functions:

X = str(X) + '\n'
F1.write(X)  # because the write function accepts string thats why X is converted to string above!
F1.write(S)
F1.flush()
F1.write(A)


# second method for writing data into a file:

L = [X, S, A]
F1.writelines(L)  # writelines() takes any collection.
F1.close()

# ----------------------------------------------------------------------------------------------------------------------
# READ-ONLY MODE:

F2 = open('out1.txt', 'r')

# if the file is not available it will not create a new file instead it willl throw a error.

r1 = F2.read()
print('r1 =\n', r1)
F2.seek(0)  # because the seek pointer traves to the end character of the txt file, in order to write again the same
# file we need to make the seek pointer 0
r2 = F2.read()
print('r2 =', r2)
F2.seek(0)
r3 = F2.readline()
print('r3 = ', r3)

while True:
    line = F2.readline()
    if line == '': # end of line.
        break
    else:
        print('line = ', line)

F2.seek(0)

r4 = F2.readlines()
print('r4 = ', r4)

r5 = []
for l in r4:
    l = l.strip()
    r5.append(l)
print('r5 =', r5)


# ---------------------------------------------------------------------------------------------------------------------

F2.seek(0)
for x in F2:
    print('line = ', x)

# ----------------------------------------------------------------------------------------------------------------------

F2.seek(0)
r6 = list(F2)

F2.seek(0)
r7 = tuple(F2)

# ----------------------------------------------------------------------------------------------------------------------

L1 = ['hi', 'h2']
L2 = ['ip1', 'ip2']

D1 = dict(zip(L1, L2))
print('D1 = ', D1)

# ----------------------------------------------------------------------------------------------------------------------

e = enumerate(L1)
print(list(e))

# ----------------------------------------------------------------------------------------------------------------------

F2.seek(0)
D2 = dict(enumerate(F2))
print('D2 =', D2)
F2.close()

# ----------------------------------------------------------------------------------------------------------------------

F3 = open('out1.txt', 'a')
F4 = open('out2.csv', 'a')  # 'a' mode (append mode) same as read but if there is no existing file then
# it creates a new file

print(20, 'java', sep='\n', file=F3, flush=True)
print(20, 'java', sep=',', file=F4)
F3.close()
F4.close()

# ----------------------------------------------------------------------------------------------------------------------

# 'w' -> write only
# 'r' -> read only
# 'a' -> append only
# 'w+' -> WR
# 'r+' -> RW
# 'a+' -> AR

# 'wb' -> write only
# 'rb' -> read only
# 'ab' -> append only
# 'w+b' -> WR
# 'r+b' -> RW
# 'a+b' -> AR