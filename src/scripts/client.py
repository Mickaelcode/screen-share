import socket 

HOST, PORT =('',5000)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((HOST, PORT))
    print('connecting client .........')

    """tranfer a data"""
    data = 'Hello'
    data = data.encode('utf8')
    socket.sendall(data)
except ConnectionAbortedError:
    print('Server error')

finally:
    socket.close()
