#!/usr/bin/python2.7
import time
import sys
import os
try:
    import pynotify
except:
    print "Please install pynotify : sudo apt-get install python-notify2"
    exit()
try:
    interface = sys.argv[1]
except:
    print "Usage: python /path/to/directory/speedshow.py [interface]"
    exit()
if "" == os.popen("ifconfig %s"%interface).read():
    exit()
c = "ifconfig %s | tail -n2"%interface
output=os.popen(c).read()
rx1 = int(output.split(" ")[11][6:])
tx1 = int(output.split(" ")[16][6:])
time.sleep(0.5)
output2=os.popen(c).read()
rx2 = int(output2.split(" ")[11][6:])
tx2 = int(output2.split(" ")[16][6:])
o = "Download : " + str((rx2 - rx1) * 2 / 1024) + " KB/s  " + "Upload : " + str((tx2 - tx1) * 2 / 1024) + " KB/s" 
pynotify.init("s")
n=pynotify.Notification("Network Speed for %s"%interface,o)
n.show()
pynotify.uninit("s") 
