import socket 

HOST, PORT =('',5000)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((HOST, PORT))
    print('connecting client .........')

except ConnectionAbortedError:
    print('Server error')

finally:
    socket.close()
