import os
from novaclient import client
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


