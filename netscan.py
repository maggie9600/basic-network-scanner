import socket
import time
import threading
import pyfiglet
import sys
   
ascii_banner = pyfiglet.figlet_format("NET SCAN")
print(ascii_banner)

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

if len(sys.argv) == 2:
      
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid ammount of Argument")
  
print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

IP = socket.gethostbyname(target)
print ('Starting scan on host: ', IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass


def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()

for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()

try:      
   for worker in range(1, 1000):
      q.put(worker)
      
   q.join()
   print('Time taken:', time.time() - startTime)

except KeyboardInterrupt:
   print("\n Exitting Program !!!!")
   sys.exit()
except socket.gaierror:
   print("\n Hostname Could Not Be Resolved !!!!")
   sys.exit()
except socket.error:
   print("\ Server not responding !!!!")
   sys.exit()