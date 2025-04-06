import numpy as np 
import pickle as pkl
from mss import mss

def send_screen(conn):
    """this function is used to send screen from the server to the client"""
    with mss() as sct :
        monitor = {'top':0, 'left':0, 'widht':800, 'height':600}
        
        while 'running':
            try:
                 img = np.array(sct.grab(monitor))

                 """encode data with pickle"""
                 img = pkl.dumps(img)
                 conn.send(img)
            except KeyboardInterrupt:
                print('finishing transfer.....')
                break
    


