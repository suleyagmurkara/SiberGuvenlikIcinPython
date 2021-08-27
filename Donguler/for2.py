# Ekrana çift sayı yazdır

sayi = int(input("Çift sayılar için üst sınır giriniz: "))

for i in range(0, sayi, 1):
    if i % 2 == 0:
        print(i)
