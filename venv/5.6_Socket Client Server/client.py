import socket

host = "127.0.0.1"
port= 2121
with socket.socket() as soket:
    soket.connect((host,port))
    soket.sendall(b'merhaba siber')
    data = soket.recv(1024)
print(data)

# Bu kod, basit bir TCP/IP soket bağlantısı oluşturarak, bir sunucuyla bağlantı kurmak, veri göndermek ve sunucudan gelen verileri okumak için kullanılır.
#
# socket modülü içe aktarılır.
# host değişkenine 127.0.0.1 IP adresi atanır.
# port değişkenine 2121 port numarası atanır.
# with bloğu içinde socket.socket() metodu kullanılarak bir soket nesnesi oluşturulur ve soket adında bir değişkene atanır.
# soket nesnesi connect() metodu ile (host, port) adresindeki bağlantı noktasına bağlanır.
# sendall() metodu, verileri gönderir. Burada, b'merhaba siber' ifadesi, bytes türünde veri göndermek için kullanılır.
# recv() metodu, soketten gelen verileri okur.
# print() fonksiyonu, sunucudan gelen verileri yazdırır.
# with bloğu sona erer ve soket otomatik olarak kapatılır.
# Bu kod, 127.0.0.1 IP adresindeki 2121 portunda bir sunucuya bağlanır ve "merhaba siber" mesajını gönderir. Sunucu, mesajı aldıktan sonra bir yanıt döndürür ve bu yanıt, data değişkenine atanır ve son olarak print() fonksiyonu tarafından yazdırılır.