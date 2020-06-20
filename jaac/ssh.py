import paramiko


def execute_command(machine_hostname, machine_port, username, password, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machine_hostname, machine_port,
                username, password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
