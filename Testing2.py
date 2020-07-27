import paramiko
import time
import getpass
import os
import re
import sys
from datetime import date
from scp import SCPClient
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


rdc = input("Please select your rdc:- Press 1 for G7R1, 2 for G7R2, 3 for G8R1, 4 for G8R2,5 for G6R1 :- ")
if rdc == "1":
    hostname = "g7r1-console.qa.xcloudiq.com"
    kube = "kubectl-g7r1"

elif rdc == "2":
    hostname = "g7r2-console.qa.xcloudiq.com"
    kube = "kubectl-g7r2"

elif rdc == "3":
    hostname = "g8r1-console.qa.xcloudiq.com"
    kube="kubectl-g8r1"

elif rdc == "4":
    hostname = "g8r2-console.qa.xcloudiq.com"
    kube="kubectl-g8r2"

elif rdc == "5":
    hostname = "g6r1-console.qa.xcloudiq.com"
    kube="kubectl-g6r1"

else:
    print("Invalid Option provided for rdc")
    sys.exit()

log = input("Please select logs to download:- Press 1 for TaskengineLogs, 2 for HmWebappLogs, 3 for CapwapLogs:- ")

ip = "134.141.85.210"

myuser = "ahqa"
mySSHK = "ahqa_id_rsa"

print("Please provide your corporate credentials:- ")

UN = input("Username : ")
PW = getpass.getpass("Password : ")
cmd1 = 'eval `ssh-agent -s`'
cmd2 = 'ssh-add ahqa_id_rsa'

os.system(cmd1)
os.system(cmd2)

ssh_client = paramiko.SSHClient()
dt = str(date.today())
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ip, port=22, username=UN, password=PW)

print("##############################################")
print("PLEASE WAIT WHILE WE COPY YOUR LOGS")
print("##############################################")
vmtransport = ssh_client.get_transport()
dest_addr = (hostname, 22)
local_addr = (ip, 22)
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)

######
time.sleep(10)
jhost = paramiko.SSHClient()
jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jhost.connect(hostname, username=myuser, key_filename =mySSHK ,sock=vmchannel)
time.sleep(5)
#####
channel = jhost.invoke_shell()
channel.send('sudo su  -\n')
time.sleep(5)
channel.send('%s get pods\n' % kube)
time.sleep(5)
while not channel.recv_ready():
    time.sleep(1)

output = channel.recv(3072)
if log == "1":
        r = re.search(r"(teall.+?) +(\d/\d) +(\w+) +(\d) +(\w+)", output)
        path = "/opt/tomcat/logs/hm.log"
        dt1 = dt + "-taskengine.log"

elif log == "2":
        r=re.search(r"(hmweb.+?) +(\d/\d) +(\w+) +(\d) +(\w+)",output)
        path="/opt/tomcat/logs/hm.log"
        dt1 = dt + "-hmweb.log"

elif log == "3":
        r=re.search(r"(capwapserver.+?) +(\d/\d) +(\w+) +(\d) +(\w+)",output)
        path="/opt/tomcat/logs/hm.log"
        dt1 = dt + "-capwapserver.log"
else:
        print("Invalid Option provided to collect logs")
        sys.exit()

str=r.group(1)
channel.send('%s cp %s:%s %s\n'%(kube,str,path,dt))
time.sleep(5)
channel.send('chmod 777 %s\n'%dt)
time.sleep(10)
channel.send('mv %s /home/ahqa/\n'%dt)
time.sleep(10)
stdin,stdout,stderr = jhost.exec_command('mv %s %s'%(dt,dt1))
time.sleep(10)
stdin,stdout,stderr = jhost.exec_command('gzip %s'%dt1)

time.sleep(5)
dt2 = dt1 + ".gz"
#####
with SCPClient(jhost.get_transport()) as scp:
    scp.get(dt2, dt2)
time.sleep(10)

stdin, stdout, stderr = jhost.exec_command('rm -f %s'% dt2)
print("LOGS DOWNLOAD COMPLETE")
time.sleep(5)
jhost.close()
ssh_client.close()
