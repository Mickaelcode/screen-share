import argparse
import os 
import pkgutil 


parser = argparse.ArgumentParser(description='show who is the server and client')
parser.add_argument('-U','--user', help='c if client or s for server')
parser.add_argument('-H', '--host', help='host machine')
parser.add_argument('-P', '--port',type=int,  help='Port for listen')
args = parser.parse_args()


module_name = ['numpy','mss','opencv-python']
for module in module_name:
    loader = pkgutil.find_loader(module)
    if not loader :
        os.system(f'pip install {module}')



if not args.host or not args.port :
    print('host and port required')

elif not args.user or args.user == 's':
    os.system(f'python3 src/scripts/server.py {args.host} {args.port}')
else:
    os.system((f'python3 src/scripts/client.py {args.host} {args.port}'))
    
    
