import socket 
import screen
import time
import sys 


HOST, PORT = (sys.argv[1], int(sys.argv[2]))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
#socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('server running...')

try:
    while True:
        socket.listen()
        conn, address = socket.accept()
        print(f'Connection from {address}')
        
        try:
            screen.send_screen(conn)
        finally:
            conn.close()
            print('Connection closed')
            
except KeyboardInterrupt:
    print("Shutting down server")
finally:
    socket.close()
