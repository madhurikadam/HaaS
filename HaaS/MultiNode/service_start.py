import pexpect
import os


print "Starting DFS Services:"
cmd="/usr/local/hadoop/sbin/start-dfs.sh"

ssh_newkey = 'Are you sure you want to continue connecting'
p=pexpect.spawn(cmd)
#time.sleep(5)
while 1 :
	j=p.expect([ssh_newkey,'password',pexpect.EOF,pexpect.TIMEOUT])
	if j!=3 :
		break
while j!=2 :
	print "I say yes"
	p.sendline('yes')
#       time.sleep(1)
        j=p.expect([ssh_newkey,'password',pexpect.EOF,pexpect.TIMEOUT])
	if j==3:
		continue
	if j==2:
		break
	if j==1 :
		print "password"
		p.sendline('root123')
		pass

print "Starting Yarn services:"
cmd="/usr/local/hadoop/sbin/start-yarn.sh"

os.system(cmd)
       
