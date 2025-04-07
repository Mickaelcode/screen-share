import socket 
import screen
import time
import sys 
from threading import Thread

class ThreadForAllClient(Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self) -> None:
        try:
            screen.send_screen(self.conn)
        finally:
            self.conn.close()
            print('Connection closed')


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
        
        thread = ThreadForAllClient(conn)
        thread.start()
            
except KeyboardInterrupt:
    print("Shutting down server")
finally:
    socket.close()
