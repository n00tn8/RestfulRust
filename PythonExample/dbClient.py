import socket
import time

HOST = 'localhost'
PORT = 51133

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:    
        try:
            send = input("\nRequest:")
            s.sendall(bytes(send, 'utf-8'))
            data = s.recv(10000)
            print('Received: ', repr(data))
        except Exception as e:
            print(f"Stopping: {e}\n")
            break
        except KeyboardInterrupt:
            print("")
            break