import socket 
import numpy as np 
import cv2
from mss import mss
import pickle

HOST, PORT =('',5000)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((HOST, PORT))
    print('connecting client .........')

    """tranfer a data"""
    with mss() as sct:
        img = np.array(sct.monitors[1])
        data = 'Hello'
        img = pickle.dumps(img)
        data = data.encode('utf8')
        socket.send(img)
except ConnectionAbortedError:
    print('Server error')

finally:
    socket.close()
