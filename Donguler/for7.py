# Üs hesaplama

us = int(input("Üs Giriniz: "))
taban = int(input("Taban Giriniz: "))
sonuc = 1

for i in range(1, us+1, 1):
    sonuc *= taban

print("Sonuç: ", sonuc)
