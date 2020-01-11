# variables args
def add(a, b = 10, *c):  # *c will accept n number of arguments. and all the extra args will be kept in tuple.
    print('Extra args passed = ', c)
    r = a + b + sum(c)
    return r


res1 = add(10)
print('res1 = ', res1)
print('-'*40)
res2 = add(10, 20, 30, 40, 50)
print('res2 = ', res2)


def telnet(host=None, port=None, *cmds):
    import subprocess
    result = []
    for each_cmd in cmds:
        r1 = subprocess.check_output(each_cmd, shell=True)  # this is used to run the shell comands.
        result.append(r1)
    return result


r = telnet(0, 0, 'dir', 'type log_report.csv')  # here r contains byte values. 'dir' and 'type og_report.txt'
# are shell commands
print('r = ', r)
f = open('cmd_out.txt', 'w')
r = [line.decode() for line in r]  # decode() is a built in function which is used to convert bytes to string.
f.writelines(r)
f.close()

# now if we want to pass the elements of a list as arguments.

c = ['dir', 'type log_report.txt']

r2 = telnet(0, 0, *c)  # unpacking.

