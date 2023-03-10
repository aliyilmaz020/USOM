import socket

host="127.0.0.1"
port=2121

with socket.socket() as soket:
    soket.bind((host,port))
    soket.listen()
    conn, addr = soket.accept()
    with conn:
        print("Baglanti yapildi",addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# Bu kod, basit bir TCP/IP soket bağlantısı oluşturarak, bir bağlantıyı dinlemek, bağlantıyı kabul etmek, gelen verileri okumak ve gelen verileri geri göndermek için kullanılır.
#
# socket modülü içe aktarılır.
# host değişkenine 127.0.0.1 IP adresi atanır.
# port değişkenine 2121 port numarası atanır.
# with bloğu içinde socket.socket() metodu kullanılarak bir soket nesnesi oluşturulur ve soket adında bir değişkene atanır.
# soket nesnesi bind() metodu ile (host, port) adresindeki bağlantı noktasına bağlanır.
# listen() metodu, istemci bağlantıları dinlemek için soketi ayarlar.
# accept() metodu, soketten gelen bağlantıyı kabul eder ve yeni bir soket nesnesi ve istemcinin adresi conn ve addr değişkenlerine atanır.
# while döngüsü, bağlantı tamamlanana kadar devam eder.
# data değişkeni conn.recv(1024) ile gelen verileri okur ve 1024 bayt kadar veri alır.
# if not data: bloğu, gelen veri yoksa döngüden çıkar.
# conn.sendall(data) metodu, gelen verileri geri gönderir.
# print() fonksiyonu, "Bağlanti yapildi" mesajını ve istemcinin IP adresini yazdırır.
# with bloğu sona erer ve soket otomatik olarak kapatılır.
# Bu kod, 127.0.0.1 IP adresindeki 2121 portunda bir soket oluşturur ve gelen verileri geri gönderir. Bu kod, aynı bilgisayar üzerinde çalışan başka bir program tarafından kullanılabilir veya bir ağ üzerindeki diğer bilgisayarlarla iletişim kurmak için de kullanılabilir.