from tkinter import *
import datetime

def kontrol_et():
    dosya = open("usom.txt","r")
    icerik = dosya.read()
    dosya.close()
    ip=entry1.get()
    bugun = datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+" zararli\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlidir.")
    else:
        dosya=open("log.txt","a")
        yazi = str(ip) + " zararli degil\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararsizdir")

top = Tk()
top.title("USOM IP Kontrolu")
B = Button(top,text="Kontrol Et",command=kontrol_et)
B.place(x=50,y=50)
B.pack()
label1 = Label(top,text = "Konrol edilecek IP yi giriniz:")
label1.place(x=50,y=50)
label1.pack()
entry1 = Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v = StringVar()
entry2 = Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()
top.mainloop()
#
# Bu kod bir GUI (grafik kullanıcı arayüzü) uygulamasıdır ve IP adresleri üzerinde zararlı IP adresleri kontrolü yapar. İşlevselliği için tkinter ve datetime modüllerini kullanır.
#
# Kodun çalışması şu şekildedir:
#
# tkinter modülü içe aktarılır
# datetime modülü içe aktarılır
# kontrol_et adında bir fonksiyon tanımlanır
# usom.txt adlı dosya açılır ve okunur
# kullanıcının entry1 widget'ına girdiği IP adresi alınır
# datetime.datetime.now() ile şu anki tarih ve saat alınır
# Eğer girilen IP adresi usom.txt dosyasındaki zararlı IP listesinde ise, log.txt dosyasına girilen IP adresi "zararlı" olarak kaydedilir, tarih/saat bilgisi de eklenir ve v değişkenindeki metin "IP zararlidir." olarak güncellenir.
# Eğer girilen IP adresi usom.txt dosyasındaki zararlı IP listesinde değilse, log.txt dosyasına girilen IP adresi "zararlı değil" olarak kaydedilir, tarih/saat bilgisi de eklenir ve v değişkenindeki metin "IP zararsizdir" olarak güncellenir.
# top adında bir tkinter penceresi oluşturulur ve pencerenin başlığı "USOM IP Kontrolu" olarak ayarlanır.
# Button widget'ı oluşturulur ve "Kontrol Et" metni ile kontrol_et fonksiyonuna bağlanır.
# Label widget'ı oluşturulur ve "Konrol edilecek IP yi giriniz:" metni ile yerleştirilir.
# Entry widget'ı oluşturulur ve kullanıcının IP adresini girmesi için kullanılır.
# StringVar sınıfı ile v adında bir metin değişkeni oluşturulur.
# Entry widget'ı oluşturulur ve v değişkeni ile bağlanır.
# Son olarak mainloop() metodu ile tkinter penceresi çalıştırılır ve kullanıcının uygulamayı kullanması sağlanır.