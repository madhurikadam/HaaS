import os
from novaclient import client
from insert_tab import *
nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")

def rebootinstance(Iname,cname):
	#nova.servers.stop(Iname)
	server = nova.servers.find(name=Iname)
	server.reboot(reboot_type='HARD')
	statusStartI(Iname,cname)

	
def rebootcluster(cname):
	count=getInstancecount(cname)
	for i in range(0,count):
		iname=cname+"-"+str(i)
		stats=getstatusI(iname)
		if stats=="TERMINATED":
			continue
		server = nova.servers.find(name=iname)
		server.reboot(reboot_type="HARD")
		statusStartI(iname,cname)
	statusStartC(cname)
		

#rebootinstance("p13-2","p13")
#rebootcluster("hello")	
