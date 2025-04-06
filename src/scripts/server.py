import socket 

HOST, PORT  = ('', 5000)

""" Create an objet socket"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
print('server running...')
"""listen the client"""
socket.listen()

"""While the server is on"""
while "SERVER_IS_ON":
    try:
        """accept the client"""
        conn, address = socket.accept()
        print('waiting for client message .........')
    except KeyboardInterrupt:
        socket.close()
        break
    except:
        socket.close()
socket.close()
