import os
import time
from novaclient import client
nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")
#print nova.servers.list()
#print nova.flavors.list()

#print nova.floating_ips.list()
#print nova.floating_ips.list()
def getfixed_ip (name1) :
	fixed_ips = [addr for addr in nova.floating_ips.list() if addr.instance_id is not None]
	#print fixed_ips
	for i in fixed_ips :
		if i.fixed_ip:
			file1=open(name1,"a+")
			file1.write(i.fixed_ip)
			#print i.fixed_ip
			file1.write("\n")
def getfloating_ip(name1):
	floating_ips = [addr for addr in nova.floating_ips.list() if addr.instance_id is not None]
        for i in floating_ips :
                if i.ip:
                        file1=open(name1,"a+")
                        file1.write(i.ip)
                        file1.write("\n")

	
#floating_ip = nova.floating_ips.create("ext-net")
#instance = nova.servers.find(name="my")
#instance.add_floating_ip(floating_ip)
                       

#getfixed_ip("rr")

