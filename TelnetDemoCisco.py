import getpass
import sys
import telnetlib
def RP_RIP2(networks):
	tn.write("conf t\n") #configuration mode
	tn.write("router rip\n")
	tn.write("version 2\n")
	tn.write("network "+networks+"\n")
	tn.write("end\n") #priviledged mode

def interface(iface,ip):
	tn.write("conf t\n") #configuration mode
	tn.write("int "+iface+"\n")
	tn.write("ip addr "+ip+" 255.255.255.0\n")
	tn.write("no sh\n")
	tn.write("end\n") #priviledged mode

SUBNET0_F00 = "192.168.0.1" #fa0/0 R1
SUBNET1_F01 = "192.168.7.1" #fa0/1 R1
SUBNET2_F10 = "192.168.8.1" #fa1/0 R1

user = raw_input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(SUBNET0_F00)
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

#user mode
tn.write("enable\n")
tn.write("cisco\n")

#priviledged mode
interface("fa0/1",SUBNET1_F01)
interface("fa1/0",SUBNET2_F10)
RP_RIP2("192.168.0.0")

tn.write("exit\n")

print tn.read_all()