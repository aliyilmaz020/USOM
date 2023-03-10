import requests

dosya = open("fuzzing.txt","r")
icerik = dosya.read()
dosya.close()
header = {"Cookie": "_cfuvid=WDlonye8yEuGHnJq0Gx9KFJVeZsmh7mTZ8ZldW27rGE-1678462147045-0-604800000"}
# print(icerik)
for i in icerik.split("\n"):
    print(i)
    url="http://10.0.2.4"+str(i)
    sonuc=requests.get(url=url,headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya ya da dizin var",i)
    else:
        print("Dosya ya da dizin yok",i)

# fuzzing: bir sunucuda ilgili dizinleri kontrol etmek için kullanılır.