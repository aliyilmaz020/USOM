import datetime
import sqlite3
import requests
import subprocess
import socket
header = {"X-ApiKeys": "accessKey=45dac1f3ced6885ee647ef6dc5db2cd6893994f0f4a261f7f6d0802f10144ebd; "
                       "secretKey= a41d94a1e4d0b2b27b795a5eac8616a4220ed7d043039b3a7d11644df4b04713;"}

cikti = subprocess.check_output("dir",shell=True)
if not "host_discovery.db" in str(cikti):
    print("Veritabanı yok")
    conn = sqlite3.connect("host_discovery.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE hosts (ip text, zaman text)''')
    c.close()
conn = sqlite3.connect("host_discovery.db")
c = conn.cursor()
c.execute('SELECT ip FROM hosts')
ipler = c.fetchall()
ipler_liste = []
for i in ipler:
    ipler_liste.append(str(i[0]))
conn.close()
url = "https://127.0.0.1:8834/scans"
sonuc = requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
    if "HD" in i['name'] and "completed" in i['status']:
        url = "https://127.0.0.1:8834/scans/"+str(i["id"])
        sonuc = requests.get(url=url,headers=header,verify=False)
        for j in sonuc.json()['hosts']:
            if not j['hostname'] in ipler_liste:
                print("Yeni IP: ",j['hostname'])
                conn = sqlite3.connect("host_discovery.db")
                c = conn.cursor()
                c.execute('INSERT INTO hosts VALUES(?,?)',(str(j['hostname']),str(datetime.datetime.now())))
                conn.close()
                s = socket.socket()
                s.connect(("10.0.2.5",515))
                log = "yeni ip bulundu: "+str(j['hostname'])
                s.sendall(str(log).encode())
                s.close()