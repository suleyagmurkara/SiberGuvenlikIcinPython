# Ekrana çift sayıları yazdır

sayi = int(input("Çift sayılar için üst sınır giriniz: "))
sayac = 0

while sayac < sayi:
    if sayac % 2 == 0:
        print(sayac)
    sayac += 1
