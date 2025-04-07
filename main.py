import argparse
import os 

parser = argparse.ArgumentParser(description='show who is the server and client')
parser.add_argument('-U','--user', help='c if client or s for server')
parser.add_argument('-H', '--host', help='host machine')
parser.add_argument('-P', '--port',type=int,  help='Port for listen')
args = parser.parse_args()


if not args.host or not args.port :
    print('host and port required')

elif not args.user or args.user is 's':
    os.system(f'python3 src/scripts/server.py {args.host} {args.port}')
else:
    os.system((f'python3 src/scripts/client.py {args.host} {args.port}'))
    
    
