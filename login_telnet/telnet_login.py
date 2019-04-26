import getpass
import sys
import telnetlib
import os
os.system("stty erase '^H'")

def auth_login(user,password):
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")
	    return True
	else :
		return False
if __name__ == "__main__":
	print("==========================================")
	print("Welcome to 'VPN app configuration' !")
	print("by Bagas Adi Pamungkas")
	print("")
	target_telnet = str(raw_input("Enter Target Telnet IP (example 10.10.1.1): "))
	user = raw_input("Enter your Telnet username: ")
	password = getpass.getpass()

	if target_telnet != "":
		global tn 
		tn = telnetlib.Telnet(target_telnet)
		login = auth_login(user,password)
		if login :
			print("Login Success!")
			tn.write("exit\n")

			print tn.read_all()

