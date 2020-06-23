import os,parser,sys,sysconfig,subprocess
import socketserver,socket
# PS Ultility
# https://www.thepythoncode.com/article/get-hardware-system-information-python#Disk_Usage
import psutil
import platform

print("_"*40)
print("Your System Information")
print("_"*40)
""" Get current system like: 
Standard Fearture: SELINUX, IP, Hostname, Firewall, Disks, mount point
"""
dict_state={}
# Function get current SE-Linux Setting
def selinux_State():
    sestatus=subprocess.run('sestatus',stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True)
    sestatus_decode=sestatus.stdout.decode()
    if str(sestatus_decode.find('disabled')):
        return 'Disabled'
    return 'Enabled'
# Funtion get IP 
def get_IPName():
    hostname=socket.gethostname()
    return socket.gethostbyname(hostname),hostname
# Check OS 
def get_OSrelease():
    return os.uname()
# Function get Firewall State
def get_FW():
    #[2] is release version 
    if get_OSrelease()[2].find('amz'):
        return f'Your OS has no Firewall ({get_OSrelease()[2]})'
    else:
        return 'Disabled'
# Funtion get Disks Drive
def get_Disks():
    # Get Disk
    disk_list=[]
    disk_mountpoint=[]
    disk=psutil.disk_partitions()
    for item in disk:
        disk_list.append(item.device)
        disk_mountpoint.append(item.mountpoint)
    return disk_list,disk_mountpoint

# Khởi tạo tuple IPHostname = function get_IPName, vì nó return 2 giá trị
IPHostname=get_IPName()
dict_state['Selinux']=selinux_State()
dict_state['Your IP']=IPHostname[0]
dict_state['Hostname']=IPHostname[1]
dict_state['Firewall']=get_FW()
dict_state['Disk List']=get_Disks()[0]
dict_state['Mount point']=get_Disks()[1]

for key,value in dict_state.items():
    #print(f"[{key}]:{value}")
    print("%s \t\t %s"%(key,value))

#for row in dict_state.items():
#    print("{:<20}| {:<20}".format(*row),sep="|")

print("_"*40)


