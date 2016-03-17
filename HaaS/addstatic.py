import os
from novaclient import client
from matchfixed import *
from noinstance import *
from insert_tab import *

nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")

def terminateInstance(iname, cname):

	float1=getFloatingip(iname)
	f=open("/home/student/coding1/floating_"+cname,"r")
	lines=f.readlines()
	f.close()

	f=open("/home/student/coding1/floating_"+cname,"w")
	for line in lines:
        	if line!=float1+"\n":
                	f.write(line)

	f.close()

              #  if(ip.name==iname):
                        #fixed1=ip.fixed_ip
	fixed1=getFixedip(iname)
        f=open("/home/student/coding1/fixed_"+cname,"r")
        lines=f.readlines()
        f.close()

        f=open("/home/student/coding1/fixed_"+cname,"w")
        for line in lines:
        	if line!=fixed1+"\n":
                	f.write(line)

        f.close()

	
	server = nova.servers.find(name=iname)
	server.delete()

	
	terminatedI(iname,cname)

def terminateCluster(cname):
	count=getInstancecount(cname)
	for i in range(count):
		iname=cname+"-"+i
	        server = nova.servers.find(name=iname)
	        server.delete()
	        terminatedI(iname,cname)
	os.remove("/home/student/coding1/floating_"+cname)
	os.remove("/home/student/coding1/fixed_"+cname)
	terminatedC(cname)



def addInstance(cname,no_inst):

	number=getinstanceno()
	totalno=number+int(no_inst)
	if totalno > 12:
        	print " This Number Of Instance Not Available"
        	print "Give The Number less than"+str(7-number)
       	 	quit()

	else:		
		count=getInstancecount(cname)
		instance_name=cname+"-"+str(count)

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
		
		name1=cname
		ip_list =nova.floating_ips.list()
                for ip in ip_list :
                        if (ip.instance_id == instance.id):
                                insertInstanceInfo(name1,ip.instance_id,instance_name,ip.ip,ip.fixed_ip,status)
				incrementCount(cname)
				fixip=ip.fixed_ip
				floatip=ip.ip
		
		fname1="fixed_"+cname
		fname2="floating_"+cname
		file1=open(fname1,"a+")
	        file1.seek(0)
   		file1.write(fixip)
		file1.write("\n")
		#file1.truncate()
        	#file1.seek(0)
        	file1.close()
        	file1=open(fname2,"a+")
        	file1.seek(0)
        	#file1.truncate()
        	#file1.seek(0)
		file1.write(floatip)
		file1.write("\n")
        	file1.close()
		#getmatch(cname)




#addInstance("say")
