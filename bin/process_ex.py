F1 = open('log_report.txt', 'w')

F2 = open('log_report.csv', 'w')

F1.write('IP\tDATE\tPICS\tURL\n')
F2.writelines(['IP', 'DATE', 'PICS', 'URL\n'])

F3 = open(r'C:\Users\lab365\Desktop\satish_python\log\serverlog.txt')
for line in F3:
    if line[:3].isdigit():
        print(line)
        sp = line.split()
        print(sp)
        ip = sp[0]
        print(ip)
        dt = sp[3]
        dt1 = dt[1:12]  # way one
        dt2 = dt[1:dt.index(':')]  # way two.
        print(ip, dt2)
        # if sp[6].startswith('/pics')
        if 'pics' in sp[6]:
            im = sp[6]
            im1 = im[6:]  #one way
            im2 = im.split('/')
            im2 = im2[-1]  #way two
            im3 = im.lstrip('/pics/')  # way three
            im4 = im.replace('/pics/','')
        else:
            im1 = 'no image'
        print(ip, dt2, im1)

        url = sp[10][1:-1]
        print(ip, dt2, im1, url, sep='\t',file=F1)
        print(ip,dt2,im1,url,sep=',',file=F2)
F1.close()
F2.close()
F3.close()
