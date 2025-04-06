import socket 
from . import screen

HOST, PORT  = ('', 5000)

""" Create an objet socket"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
print('server running...')
"""listen the client"""
socket.listen()

try:
    conn, adress = socket.accept()
    print(f'address= {adress} ------------ listen to the client...........')
    screen.send_screen(conn)
    conn.close()
    print('leave the function')
except:
    socket.close()

socket.close()
