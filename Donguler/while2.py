# Faktöriyel hesaplama

sayi = int(input("Faktöriyeli hesaplanacak sayı: "))
sayac = 1
faktoriyel = 1

while sayac <= sayi:
    faktoriyel *= sayac
    sayac += 1
print(faktoriyel)
