import os
from novaclient import client
from insert_tab import *
from terminatedI import *
nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")


def terminateCluster(cname):
        count=getInstancecount(cname)
        for i in range(count):
                iname=cname+"-"+str(i)
                server = nova.servers.find(name=iname)
                server.delete()
                terminatedI(iname,cname)
        os.remove("/home/student/coding1/floating_"+cname)
        os.remove("/home/student/coding1/fixed_"+cname)
        terminatedC(cname)

cname=raw_input("Enter cluster name:")
terminateCluster(cname) 
