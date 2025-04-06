import numpy as np 
import pickle as pkl
from mss import mss

def send_screen(conn):
    """this function is used to send screen from the server to the client"""
    with mss() as sct :
        monitor = {'top':0, 'left':0, 'widht':800, 'height':600}
        
        while 'sending':
            try:
                 img = np.array(sct.grab(monitor))

                 """encode data with pickle"""
                 img = pkl.dumps(img)
                 conn.send(img)
            except KeyboardInterrupt:
                print('finishing transfer.....')
                break
    


def receive_screen(socket):
    """this function is used to receive_screen from the server in the client"""
    while 'receving':
        try:
            img = socket.recv(1024)
            img = pkl.loads(img)
            print(f'img = {img}')
        except KeyboardInterrupt:
            print('Finishing receve .......')
            break


