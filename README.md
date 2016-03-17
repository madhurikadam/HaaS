Hadoop as a service over openstack private cloud.


Before using this project follow the steps below

Download Hadoop 2.6.0 and store it to MuLtinode folder which is present in this project code.
download from  https://archive.apache.org/dist/hadoop/core/hadoop-2.6.0/

Download java oracle 8 (jdk-8u5-linux-x64.tar.gz) and store it to MuLtinode folder which is present in this project code.

Steps to use HaaS over openstack :
1) Setup the openstack private cloud
2) Download the code i.e HaaS.zip
3) Extract and descend into it.
4) Perform above download steps of Hadoop and Java 8
5) Execute the following commands to launch a cluster
        python launchFixed.py
6) To add a node to existing cluster
        python addstatic.py
7) To remove a node from cluster
        python terminatedI.py
8) To remove the Cluster  
        python terminatedC.py
9) 
