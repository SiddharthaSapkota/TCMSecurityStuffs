import sys 
import socket
from datetime import datetime
import threading


#Function  to scan a port

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port)) #error indicatior - if 0, port is open else close
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}:{e}")
    except Exception as e:
        print(f"Unexcepted error on port{port}: {e}")

#Main function - argument validation and target defination

def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]

    
