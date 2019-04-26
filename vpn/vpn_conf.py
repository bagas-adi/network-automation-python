import getpass
import sys
import telnetlib
import os
os.system("stty erase '^H'")

def crypto_isakmp(ip_dst,nama_key="vpnxyz",nama_network="jkt-sby",nama_crypto_map="vpn-ngn"):
	tn.write("conf t\n") #configuration mode
	tn.write("crypto isakmp policy 1\n")
	tn.write("encr 3des\n")
	tn.write("authentication pre-share\n")
	tn.write("group 2\n")
	tn.write("exit\n")
	tn.write("crypto isakmp key "+nama_key+" address "+ip_dst+"\n")
	tn.write("crypto ipsec transform-set 6 esp-3des esp-sha-hmac\n")
	tn.write("exit\n")
	tn.write("crypto map "+nama_crypto_map+" 1 ipsec-isakmp\n")
	tn.write("set peer "+ip_dst+"\n")
	tn.write("set transform-set 6\n")
	tn.write("match address "+nama_network+"\n")
	tn.write("end\n") #priviledged mode

def nacl( ip_src, wcard_src, ip_dst, wcard_dst,nama_network="jkt-sby"):
	tn.write("conf t\n") #configuration mode
	tn.write("ip access-list extended "+nama_network+"\n")
	tn.write("permit ip "+ip_src+" "+wcard_src+" "+ip_dst+" "+wcard_dst+"\n")
	tn.write("end\n") #priviledged mode

def vpn_gateway(iface,network_ip_dst,network_subnet_dst,peer_ip_dst,nama_crypto_map="vpn-ngn"):
	tn.write("conf t\n") #configuration mode
	tn.write("int "+iface+"\n")
	tn.write("crypto map "+nama_crypto_map+"\n") 
	tn.write("exit\n")
	tn.write("ip route "+network_ip_dst+" "+network_subnet_dst+" "+peer_ip_dst+"\n")
	tn.write("end\n") #priviledged mode

def auth_login(user,password):
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")
	    return true
	else :
		return false
if __name__ == "__main__":
	print("==========================================")
	print("Welcome to 'VPN app configuration' !")
	print("by Bagas Adi Pamungkas")
	print("")
	target_telnet = raw_input("Enter Target Telnet IP (example 10.10.1.1): ")
	user = raw_input("Enter your Telnet username: ")
	password = getpass.getpass()

	if target_telnet != "":
		global tn 
		tn = telnetlib.Telnet(target_telnet)
		login = auth_login(user,password)
		if login :
			print("Login Success!")
			#user mode
			tn.write("enable\n")
			tn.write("cisco\n")

			#input after login 
			print("")
			print("Access-list Configuration ==========================================")
			network_ip_src = raw_input("Enter Network IP Source (example 10.10.1.0): ")
			network_wcard_src = raw_input("Enter Network Wildcard Source (example 0.0.0.255): ")
			network_ip_dst = raw_input("Enter Network IP Destination (example 10.30.1.0): ")
			network_wcard_dst = raw_input("Enter Network Wildcard Destination (example 0.0.0.255): ")
			print("")
			print("Crypto & Gateway Configuration ==========================================")
			iface = raw_input("Enter Your interface as VPN Gateway (fa0/0): ") 
			nama_network = raw_input("Enter Network Name (jkt-sby): ") 
			peer_ip_dst = raw_input("Enter your peer router's IP (example 192.168.1.2): ") 
			network_subnet_dst = raw_input("Enter your peer router's subnet (example 255.255.255.0): ") 

			nama_key =  raw_input("Enter VPN Key Name (vpnxyz): ") 
			nama_crypto_map =  raw_input("Enter Crypto Map Name (vpn-ngn): ") 

			#configuration
			nacl(network_ip_src,network_wcard_src,network_ip_dst,network_wcard_dst,nama_network)
			crypto_isakmp(peer_ip_dst,nama_key,nama_network,nama_crypto_map)
			vpn_gateway(iface,network_ip_dst,network_subnet_dst,peer_ip_dst,nama_crypto_map)

			tn.write("exit\n")

			print tn.read_all()

