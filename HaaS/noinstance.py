import os
import time
from novaclient import client

def getinstanceno():

	nova = client.Client("2", "demo", "root123", "demo", "http://controller:35357/v2.0")

	#print the list of existing Instances
	print nova.servers.list()
	arr=nova.servers.list()
	number=len(arr)
	return number

 
