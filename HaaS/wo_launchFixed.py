import os
import time
from novaclient import client
from variable import *
from matchfixed import *
from noinstance import *
from insert_tab import *


arg=int(instance_no)
arg1=arg
number=getinstanceno()
totalno=number+arg
if totalno > 7:
        print " This Number Of Instance Not Available"
	print "Give The Number less than"+str(7-number) 
        quit()


else :
	status="ACTIVE"
        insertClusterInfo(name1,status,arg1)
	incr=0
	getcheck()
	while arg!=0:
		instance_name=name1+"-"+str(incr)
		print instance_name

		if not nova.keypairs.findall(name="demo-key"):
		    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
			nova.keypairs.create(name="mykey", public_key=fpubkey.read())
		image = nova.images.find(name="ubuntu14")
		flavor = nova.flavors.find(name="m1.small")
		instance = nova.servers.create(name=instance_name, image=image, flavor=flavor, key_name="demo-key")

		# Poll at 5 second intervals, until the status is no longer 'BUILD'
		status = instance.status
		while status == 'BUILD':
		    time.sleep(5)
		    instance = nova.servers.get(instance.id)
		    status = instance.status
		print "status: %s" % status
		
		

		############Floating Ip associate
		unused_ips = [addr for addr in nova.floating_ips.list() if addr.instance_id is None]
		if len(unused_ips):
			floating_ip=unused_ips[0]
			instance = nova.servers.find(name=instance_name)
			instance.add_floating_ip(floating_ip)
		else:
			floating_ip = nova.floating_ips.create("ext-net")
			instance = nova.servers.find(name=instance_name)
			instance.add_floating_ip(floating_ip)

		print nova.servers.list()

		ip_list =nova.floating_ips.list()
		for ip in ip_list :
			if (ip.instance_id == instance.id):
				insertInstanceInfo(name1,ip.instance_id,instance_name,ip.ip,ip.fixed_ip,status)
		
		incr=incr+1
		arg=arg-1

	getmatch(name1)
	execfile("wo_sshcon.py")
