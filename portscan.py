import socket
import sys
import threading
from time import perf_counter

if __name__ == "__main__":
	target = sys.argv[1] if len(sys.argv) > 1 else str(input("\_> Please enter the IP: "))
ip = socket.gethostbyname(target)
print("   \_>Searching for open ports, this could take some time.")
start = perf_counter() 
print(f"\n    ------------------------\n    | Open Ports report:\n    |\n    | IP: {ip}\n    |")

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    try:
        connection = s.connect((target,port))
        print(f"    | Port: {port} is open.")
        connection.close()  
    except: 
        pass
port = 1 

for x in range(1,120000): 

    thread = threading.Thread(target=scan,kwargs={'port':port}) 

    port += 1
    try:
        thread.start() 
    except: pass

end = perf_counter()   
print("    ------------------------")
print(f"    \n\_> Ended! Time: {round(end-start)} seconds")
