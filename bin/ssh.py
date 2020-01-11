import paramiko as p

client = p.SSHClient()
client.set_missing_host_key_policy(
    p.AutoAddPolicy)  # because we cannot acces random servers other than the known we auto add the servers using this command!
client.connect('test.rebex.net', username='demo', password='password', port=22)
stdin, out, err = client.exec_command('ls')
cmd_out = out.read()
print('cmd_out =', cmd_out)

ftp = client.open_sftp()
ftp_out = ftp.get('readme.txt', 'ftp_readme.txt')
print('ftp_out = ', ftp_out)
ftp.put('out1.txt',
        'out1.txt')  # this allows us to copy the file out1.txt to the server with same filename...and file can be saved with some other name.
