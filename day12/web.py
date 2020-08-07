#!/usr/bin/python3
import cgi
import subprocess

# Put this script in /var/www/cgi-bin/ directory in your linux server
# Also add the following line in the /etc/sudoers
# docker ALL=(ALL) NOPASSWD: ALL
# apache ALL=(ALL) NOPASSWD: ALL
# Mind the spaces in the above line
# Also run the following command if you are using RHEL7 or RHEL8
# setenforce 0
# systemctl stop firewalld

myData = cgi.FieldStorage()
myimage = myData.getvalue("i")
myos = myData.getvalue("o")
myCommand = "docker run -dit --name {} {}".format(myos, myimage)

print("Content-Type:text/html")
print()
print()

print(myCommand)
print(subprocess.getoutput("sudo " + myCommand))
print("Successful !!!")
