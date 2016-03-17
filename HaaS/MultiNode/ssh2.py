import pexpect
import time
import sys
import os
#from variable import get_variable_name
#import launch
#print str(sys.argv[1])

if not os.path.isfile("/root/.ssh/id_rsa"):
	cmd="ssh-keygen -N '' -t rsa -f /root/.ssh/id_rsa"
	os.system(cmd)
	print "SSHKEY generated"
else:
	print "Key is present"
#os.system(cmd)
if not os.path.isdir("/home/student/.ssh"):
	cmd="mkdir /home/student/.ssh"
	os.system(cmd)
	print "/home/student/.ssh directory created"
else:
	print "/home/student/.ssh directory exist"
#file2="/home/student/var.txt"
filevar=open("/home/student/var.txt","r")
var=filevar.readlines()
length=len(var)
for i in range(length):
	var[i]=var[i].rstrip('\n')
filename="fixed_"+var[0]
print filename
print var[2]
print var[0]

filename1="/home/"+str(var[2])+"/"+filename
f=open(filename1,"r")
ips=f.readlines()
print ips
f.close()
length=len(ips)

#ip=ips[0]
#print ip

ssh_newkey = 'Are you sure you want to continue connecting'
count=0
i=0
while i<length :
	cmd='ssh-copy-id -i /root/.ssh/id_rsa.pub '+ips[i]
	print cmd
	p=pexpect.spawn(cmd)
	time.sleep(5)
	j=p.expect([ssh_newkey,'password:',pexpect.EOF,pexpect.TIMEOUT])
	if j==0:
		print "I say yes"
		p.sendline('yes')
#		time.sleep(1)
		j=p.expect([ssh_newkey,'password:',pexpect.EOF,pexpect.TIMEOUT])
	if j==1:
		print "I give password",
		p.sendline("root123")
		p.expect(pexpect.EOF)
	elif j==2:
		print "I either got key or connection timeout"
		pass
	if (j==3 and count<5):
		print "Time out .... trying again"
		count=count+1
		continue
	print p.before
	count=0
	i=i+1


#execfile("host_m.py")


