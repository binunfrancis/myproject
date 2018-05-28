import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.203', port=22, username='server', password='Vinu@ss123')
stdin, stdout, stderr =ssh.exec_command('ls')
output = stdout.readlines()
type(output)
print ('\n'.join(output))