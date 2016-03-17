#!/bin/bash

user="student"
##########################Prerequisties

#1.Installing Oracle Java 8

echo "Installing Java 8:"
#add-apt-repository ppa:webupd8team/java
#apt-get update
#apt-get install oracle-java8-installer
#apt-get update
#apt-get -y install openjdk-7-jdk
cd /home/$user/MultiNode
#tar -xvzf java-8-oracle.tar.gz
#mv java-8-oracle /usr/lib/jvm/.

mkdir /opt/jdk
tar -zxf jdk-8u5-linux-x64.tar.gz -C /opt/jdk
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_05/bin/java 100
update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_05/bin/javac 100
update-alternatives --install /usr/bin/jps jps /opt/jdk/jdk1.8.0_05/bin/jps 100
############It will install java source in your machine at /usr/lib/jvm/java-8-oracle

##############HDUSER

#addgroup hadoop
#adduser --ingroup hadoop hduser
#usermod -a -G hduser
#2.ssh
#3. Disable IPv6

echo "# disable ipv6
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1" >>/etc/sysctl.conf


#############################################################################################
##################INSTALLATION####################
##Untar the hadoop

echo "Unzip hadoop tar file"
tar -xzvf /home/$user/MultiNode/hadoop-2.6.0.tar.gz >/dev/null

echo "Move hadoop folder to /usr/local/hadoop"
mv /home/$user/MultiNode/hadoop-2.6.0 /usr/local/hadoop

echo "Give ownership to /usr/local/hadoop"
#chown student -R /usr/local/hadoop 


echo "Again assign ownership of this Hadoop temp folder to Hadoop user"
#chown student -R /usr/local/hadoop_tmp/


###############Update configuration file

echo "# -- HADOOP ENVIRONMENT VARIABLES START -- #
export JAVA_HOME=/opt/jdk/jdk1.8.0_05
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
# -- HADOOP ENVIRONMENT VARIABLES END -- #" >>/home/student/.bashrc

source /home/student/.bashrc
#################################################################################
#####Update JAVA_HOME variable in /usr/local/hadoop/etc/hadoop/hadoop-env.sh

echo "export JAVA_HOME=/opt/jdk/jdk1.8.0_05" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh



rm /usr/local/hadoop/etc/hadoop/core-site.xml
cp /home/student/MultiNode/core-site.xml /usr/local/hadoop/etc/hadoop/core-site.xml

rm /usr/local/hadoop/etc/hadoop/hdfs-site.xml
cp /home/student/MultiNode/hdfs-site.xml /usr/local/hadoop/etc/hadoop/hdfs-site.xml

rm /usr/local/hadoop/etc/hadoop/yarn-site.xml
cp /home/student/MultiNode/yarn-site.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml

touch /usr/local/hadoop/etc/hadoop/mapred-site.xml
cp /home/student/MultiNode/mapred-site.xml /usr/local/hadoop/etc/hadoop/mapred-site.xml


touch /usr/local/hadoop/etc/hadoop/dfs.exclude
