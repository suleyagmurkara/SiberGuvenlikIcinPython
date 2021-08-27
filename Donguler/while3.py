# Toplama

sayi = int(input("Sayı Giriniz: "))
sayac = 0
toplam = 0
while sayac < sayi:
    toplam += sayac
    sayac += 1
print("Sonuç: ", str(toplam))
