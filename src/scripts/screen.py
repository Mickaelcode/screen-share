import numpy as np 
import time
import pickle as pkl
from mss import mss
import struct
import cv2 as cv 


def send_screen(conn):
    """Send screen from server to client with proper framing"""
    with mss() as sct:
        monitor = {'top': 0, 'left': 0, 'width': 800, 'height': 600}
        
        while True:
            try:
                
                img = np.array(sct.grab(monitor))
                img_data = pkl.dumps(img)
                conn.sendall(struct.pack('!I', len(img_data)))
                conn.sendall(img_data)
                time.sleep(0.05)
                
            except (ConnectionError, BrokenPipeError):
                print("Client disconnected")
                break
            except KeyboardInterrupt:
                print("Stopping screen sharing")
                break
            except Exception as e:
                print(f"Error: {e}")
                break



def receive_screen(socket):
    """Receive screen from server with proper framing"""
    while True:
        try:
            # First receive the length (4 bytes)
            raw_len = recv_all(socket, 4)
            if not raw_len:
                break
            msg_len = struct.unpack('!I', raw_len)[0]
            
            # Then receive the actual data
            img_data = recv_all(socket, msg_len)
            if not img_data:
                break
                
            # Deserialize
            img = pkl.loads(img_data)
            print(f"Received image with shape: {img.shape}")
            
        except ConnectionError:
            print("Server disconnected")
            break
        except KeyboardInterrupt:
            print("Stopping reception")
            break
        except Exception as e:
            print(f"Error: {e}")
            break



def recv_all(sock, n):
    """Helper function to receive exactly n bytes"""
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


def show_screen(img):
    cv.imshow('screen',img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        cv.destroyAllWindows()
