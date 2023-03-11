import requests
import subprocess
import datetime
import sqlite3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cikti = subprocess.check_output("ls",shell=True)
if not "port.db" in str(cikti):
    conn = sqlite3.connect('port.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE portlar (port text, ip text, zaman text)''')
    c.close()
header = {"X-ApiKeys": "accessKey=b88db520d0b1358342f3d9b207f78724b01fae03c37efcc587861de50546ccc2; "
                       "secretKey=f218eb56f0f3f08c51e2ab7f381c47e15bb48668ccb9b894745318ac92937b10"};
url = "https://127.0.0.1:8834/scans"
sonuc = requests.get(url=url,headers=header,verify=False)
# print(sonuc.json())
for i in sonuc.json()['scans']:
    scan_id = i['id']
    url = "https://127.0.0.1:8834/scans/"+str(scan_id)
    tarama = requests.get(url=url,headers=header,verify=False)
    # print(tarama.json())
    for j in tarama.json()['hosts']:
        try:
            host_id = j['host_id']
            #14272 açık portları gösterir
            url = "https://127.0.0.1:8834/scans/"+str(scan_id)+"/hosts/"+str(host_id)+"/plugins/11219"
            IP = requests.get(url=url,headers=header,verify=False)
            # print(IP.json())
            for k in IP.json()['outputs']:
                # print(k)
                # port = list(k['ports'].keys())[0]
                port = list(k['ports'].keys())[0]
                # print(port)
                IP = j['hostname']
                # print(IP)
                conn = sqlite3.connect("port.db")
                c = conn.cursor()
                cikti = c.execute("SELECT * FROM portlar WHERE port=? AND ip=?", (port, IP))
                port_sayisi = len(cikti.fetchall())
                conn.close()
                if port_sayisi<1:
                    print("Yeni port: ",port,"IP: ",IP)
                    conn = sqlite3.connect("port.db")
                    c = conn.cursor()
                    c.execute('INSERT INTO portlar VALUES (?,?,?)',(port,IP,str(datetime.datetime.now())))
                    conn.commit()
                    conn.close()

        except:
            pass
