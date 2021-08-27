# Asal Sayılar

sayi = int(input("Asal sayı için üst sınır giriniz: "))
print(2)
sayac = 0

for i in range(3, sayi, 1):
    kontrol = False
    for j in range(2, i):
        if i % j == 0:
            kontrol = True
    if kontrol == False:
        print(i)

