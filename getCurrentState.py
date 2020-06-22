import os,parser,sys,sysconfig,subprocess
import socketserver,socket
# PS Ultility
import psutil

print("_"*40)
""" Get current system like: 
Standard Fearture: SELINUX, IP, Hostname, Firewall, Disks, FSTab
"""
dict_state={}
# Function get current SE-Linux Setting
def selinux_State():
    sestatus=subprocess.run('sestatus',capture_output=True,check=True)
    if str(sestatus).find('disabled'):
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
        return 'Your OS has no Firewall'
    else:
        return 'Disabled'
# Funtion get Disks Drive
def get_disks():
    disk=psutil.get_disks()
    return

# Khởi tạo tuple IPHostname = function get_IPName, vì nó return 2 giá trị
IPHostname=get_IPName()
dict_state['Selinux']=selinux_State()
dict_state['IP']=IPHostname[0]
dict_state['Hostname']=IPHostname[1]
dict_state['Firewall']=get_FW()

# print(dict_state)
# for key,value in dict_state.items():
#     print(f"[{key}]:{value}")

for row in dict_state.items():
    print("|{:<20}|{:<20}".format(*row),sep="|")

print("_"*40)
print(psutil.get_disks())
