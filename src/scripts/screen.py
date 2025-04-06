import numpy as np 
import cv2 as cv
from mss import mss

def send_screen(conn):
    """this function is used to send screen from the server to the client"""
    with mss() as sct :
        monitor = {'top':0, 'left':0, 'widht':800, 'height':600}

