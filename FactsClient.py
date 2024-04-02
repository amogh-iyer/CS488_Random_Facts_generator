import socket

HOST = "127.0.0.1"
PORT = 5555

while True:
 msg = input("What do you want a fact about (cats, dogs, sloths, biriyani or quit): ")
 if msg == 'quit':
  print('User wants to exit.')
  break

 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect((HOST, PORT))
 client.sendall(msg.encode())
 data = client.recv(1024)
 client.close()

 print(data.decode())