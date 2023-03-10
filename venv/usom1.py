import requests

response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
dosya = open("usom.txt","w")
dosya.write(str(response.content))
dosya.close()
# Bu Python kodu, "requests" adlı bir kütüphaneyi kullanarak belirtilen URL'den (https://www.usom.gov.tr/url-list.txt) veri alır ve bu veriyi "usom.txt" adlı bir dosyaya yazdırır.
#
# İlk satırda, "requests" kütüphanesi dahil edilir.
#
# İkinci satırda, "requests.get" metodu kullanılarak belirtilen URL'den veri alınır. Bu veri, "response" adlı değişkene atanır.
#
# "verify=False" ifadesi,
# HTTPS bağlantısının doğrulanmasını devre dışı bırakır.
# Bu, veri kaynağına güvenilir bir bağlantı yapılamadığında kullanılabilir. Ancak, güvenli olmayan bağlantıları kullanmak güvenlik riski taşıdığından, bu kullanım önerilmez.
#
# Üçüncü satırda, "usom.txt" adlı bir dosya açılır ve "w" (yazma) modunda açıldığı belirtilir.
#
# Dördüncü satırda, "dosya.write" yöntemi kullanılarak "response.content" içeriği dosyaya yazdırılır.