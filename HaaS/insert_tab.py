#!/usr/bin/python
import MySQLdb
import sys
import csv

connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "root123", db = "Hadoop")

# prepare a cursor object using cursor() method
c = connection.cursor ()

def insertClusterInfo(name,status,instance_count):

	c.execute('''insert into ClusterInfo (c_name,c_status,no_instance) values(%s,%s,%s)''',(name,status,instance_count))
	
	# close the cursor object
	# c.execute("select * from ClusterInfo")
	#c.execute(add)
	connection.commit()
def displayClusterInfo():
	c.execute("select * from ClusterInfo")
        for i in range(c.rowcount):
                row=c.fetchone()
                print row[0],row[1],row[2],row[3]
    


def insertInstanceInfo(cname,i_id,i_name,floating_ip,fixed_ip,status):
	c.execute("select * from ClusterInfo where c_name=%s",(cname)) 
        row =c.fetchone()
	c_id=row[0]
	c.execute('''insert into InstanceInfo(c_id,i_id,i_name,floating_ip,fixed_ip,i_status) values(%s,%s,%s,%s,%s,%s)''',(c_id,i_id,i_name,floating_ip,fixed_ip,status))

        # close the cursor object
        # c.execute("select * from ClusterInfo")
        #c.execute(add)
        connection.commit()
	print "DataInserted Successfully"

#insertClusterInfo("saaaa","active",1)
#
#displayClusterInfo()
#c.close ()
#insertInstanceInfo("wer",12,"mad","11,11.1.1","192.12.1.3","ACTIVE")

#i close the connection
#connection.close ()

# exit the program
#sys.exit()

def getInstancecount(cname):
	c.execute("select no_instance from ClusterInfo where c_name=%s",(cname))
	count=c.fetchone()
	return count[0]

def getstatusI(iname):
	c.execute("select i_status from InstanceInfo where i_name=%s",(iname))
	status=c.fetchone()
	return status[0]

def getstatusC(cname):
	c.execute("select c_status from ClusterInfo where c_name=%s",(cname))
        status=c.fetchone()
        return status[0]
	
def statusStopI(iname,cname):
	status=getstatusI(iname)
	if (status == "ACTIVE"):
		sta="SHUTDOWN"
		c.execute("update InstanceInfo set i_status=%s where i_name=%s",(sta,iname))
		connection.commit()
	count=getInstancecount(cname)
	flag=0
	for i in range(count):
		name=cname+"-"+str(i)
		sta1=getstatusI(name)
		if (sta1== "ACTIVE"):
			flag=1
			break
	if flag==0:
		statusStopC(cname)	
		
	
def statusStopC(cname):
	status=getstatusC(cname)
	if(status == "ACTIVE"):
		sta="SHUTDOWN"
		c.execute("update ClusterInfo set c_status=%s where c_name=%s",(sta,cname))
		connection.commit()	


def statusStartI(iname,cname):
        status=getstatusI(iname)
        if (status == "SHUTDOWN"):
                sta="ACTIVE"
                c.execute("update InstanceInfo set i_status=%s where i_name=%s",(sta,iname))
                connection.commit()
        	statusStartC(cname)

def statusStartC(cname):
        status=getstatusC(cname)
        if(status == "SHUTDOWN"):
                sta="ACTIVE"
                c.execute("update ClusterInfo set c_status=%s where c_name=%s",(sta,cname))
                connection.commit()
def terminatedI(iname,cname):
	count=getInstancecount(cname)
	st1="TERMINATED"
	c.execute("update InstanceInfo set i_status=%s where i_name=%s",(st1,iname))
	connection.commit()
	count=count-1
	c.execute("update ClusterInfo set no_instance=%s where c_name=%s",(count,cname))
	connection.commit()
	if (count==0):
		terminatedC(cname)


def terminatedC(cname):
	st2="TERMINATED"
	c.execute("update ClusterInfo set c_status=%s where c_name=%s",(st2,cname))
	connection.commit()


def getFloatingip(iname):
	if ((getstatusI(iname))!="TERMINATED"):
		c.execute("select floating_ip from InstanceInfo where i_name=%s",(iname))
		var=c.fetchone()
		return var[0]
	else:
		print "Already TERMINATED!!"
		sys.exit()



def getFixedip(iname):
	if ((getstatusI(iname))!="TERMINATED"):
		c.execute("select fixed_ip from InstanceInfo where i_name=%s",(iname))	
		var1=c.fetchone()
		return var1[0]
	else:
		print "Already TERMINATED!!"
		sys.exit()

def incrementCount(cname):
	count=getInstancecount(cname)
	count=count+1
	c.execute("update ClusterInfo set no_instance=%s where c_name=%s",(count,cname))
	connection.commit()
	
