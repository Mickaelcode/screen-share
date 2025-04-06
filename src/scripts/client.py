import socket
import screen
import time
import sys 


HOST, PORT = (sys.argv[1], int(sys.argv[2]))  

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((HOST, PORT))
    print('Connected to server')
    screen.receive_screen(socket)
    
except ConnectionRefusedError:
    print("Could not connect to server")
except ConnectionAbortedError:
    print("Server error")
except KeyboardInterrupt:
    print("Client stopped")
finally:
    socket.close()
