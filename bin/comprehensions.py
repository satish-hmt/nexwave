# Passing expressions in Lists, Tuples, dictionaries instead of directly passing the values.
L1 = [i for i in range(10)]
L2 = [i*i for i in L1 if i%2 == 0]
F = open('out1.txt')
L3 = [line.strip() for line in F]
print(L3)
F2 = open(r'C:\Users\lab365\Desktop\satish_python\log\serverlog.txt')
IP = [line.split()[0] for line in F2 if line[:3].isdigit()]
print(IP)
F2.seek(0)
IP2 = (line.split()[0] for line in F2 if line[:3].isdigit())
print(list(IP2))
F2.seek(0)
images = [line.split()[6].lstrip('/pics/') if 'pics' in line.split()[6] else 'no image' for line in F2 if line[:3].isdigit()]
print(images)

hosts = ['hi', 'h2']
ips = ['ip1', 'ip2']
D = {K:V for K,V in zip(hosts, ips)}
print(D)