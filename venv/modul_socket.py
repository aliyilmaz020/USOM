import socket

port_list = []
banner_list = []

dosya = open("ip.txt", "r")
ipler = dosya.read()
dosya.close()
for ip in ipler.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            soket = socket.socket()
            soket.connect((str(ip),int(port)))
            banner = soket.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("Sistem linux ya da network cihazı olabilir")
                log = str(ip)+"\n"
                dosya = open("linux.txt", "a")
                dosya.write(log)
                dosya.close()
        except:
            pass
print(port_list)
print(banner_list)