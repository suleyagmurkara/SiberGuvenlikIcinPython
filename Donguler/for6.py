# Girilen sayıya kadar toplam al

sayi = int(input("Sayı Giriniz: "))
toplam = 0

for i in range(1, sayi, 1):
    toplam += i
print(toplam)
