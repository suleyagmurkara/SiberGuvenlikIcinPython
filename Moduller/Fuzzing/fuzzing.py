import requests

dosya = open("fuzzing.txt", "r")
icerik = dosya.read()
dosya.close()

header = {"Cookie": "security=impossible; security=impossible; PHPSESSID=6kesira4k6fa4v998j4d85g19e"}

for i in icerik.split("\n"):
    print(i)
    url = "http://127.0.0.1" + str(i)
    sonuc = requests.get(url=url, headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var: ", i)
    else:
        print("Dosya veya dizin yok: ", i)
