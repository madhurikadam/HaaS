import os
import sys
import shutil

rm_no=sys.argv[2]
rm_no=int(rm_no)

length=sys.argv[1]
length=int(length)

delete=[""]*rm_no
for i in range(rm_no):
        delete[i]="HadoopSlave"+str(length-i-1)

print delete


src=['/etc/hosts','/usr/local/hadoop/etc/hadoop/slaves']
src_l=len(src)

for i in range(src_l):
        shutil.copy2(src[i],'/home/student/MultiNode/check')

        with open('/home/student/MultiNode/check') as oldfile, open('/home/student/MultiNode/check1', 'w') as newfile:
                for line in oldfile:
                        if not any(d in line for d in delete):
                                newfile.write(line)

        shutil.copy2('/home/student/MultiNode/check1',src[i])
        

#        shutil.copy2('/home/student/MultiNode/check1',src[i])

 
