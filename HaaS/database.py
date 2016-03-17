import os
from novaclient import client

nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/")

f=open("floating_hello","r")
lines=f.readlines()
f.close()

f=open("floating_hello","w")
for line in lines:
	if line!="11.11.4.45"+"\n":
		f.write(line)

f.close()
