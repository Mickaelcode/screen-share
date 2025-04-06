import socket 
import pickle


HOST, PORT  = ('', 5000)

""" Create an objet socket"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
print('server running...')
"""listen the client"""
socket.listen()

"""While the server is on"""
while True:
    try:
         conn, address = socket.accept()
         print('waiting for client message .........')
         data = conn.recv(1024)
         data = pickle.loads(data)
   # data = data.decode('utf8')
   # print(f'client message : {data}')
         print(data)
    except KeyboardInterrupt:
        socket.close()
    except:
        socket.close()


socket.close()
