#from var import *

#def set_variables():
f=open("var.txt","wb")
name1=raw_input("Name of cluster: ")
f.write(name1+"\n")
instance_no=raw_input("Number of instances: ")
f.write(instance_no+"\n")
user=raw_input("User name: ")
f.write(user+"\n")
user_passwd=raw_input("User passwd: ")
f.write(user_passwd+"\n")
root_passwd=raw_input("Root passwd: ")
f.write(root_passwd+"\n")
f.close()



