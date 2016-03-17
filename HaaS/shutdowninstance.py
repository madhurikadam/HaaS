import os
from novaclient import client
from insert_tab import *
nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")

def stopinstance(Iname,cname):
	#nova.servers.stop(Iname)
	server = nova.servers.find(name=Iname)
	my_ip=nova.servers.list()
        for ip in my_ip:
 	       if(ip.name==Iname):
        		status=ip.status
                        if(status=="ACTIVE"):
				server.stop()
				#cname="had"
				statusStopI(Iname,cname)
	
def stopcluster(cname):
	count=getInstancecount(cname)
	for i in range(0,count):
		iname=cname+"-"+str(i)
		stats=getstatusI(iname)
		if(stats=="TERMINATED"):
			continue
		server = nova.servers.find(name=iname)
		my_ip=nova.servers.list()
                for ip in my_ip:
                        if(ip.name==iname):
                                status=ip.status
                                if(status=="ACTIVE"):
					server.stop()
					statusStopI(iname,cname)
	statusStopC(cname)
		

#startinstance("hello-0","hello")
#stopinstance("p13-2","p13")
#stopcluster("hello")	
