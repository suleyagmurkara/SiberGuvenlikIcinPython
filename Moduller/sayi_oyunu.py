import random

random_sayi = round(random.random()*100)
print(random_sayi)

girilen_sayi = int(input("0-100 arasında sayı giriniz: "))

while random_sayi != girilen_sayi:
    if girilen_sayi > random_sayi:
        print("Büyük bir sayı girdiniz.")
    else:
        print("Küçük bir sayı girdiniz.")
    girilen_sayi = int(input("0-100 arasında sayı giriniz: "))

print("Tebrikler! Oyunu kazandınız.")
