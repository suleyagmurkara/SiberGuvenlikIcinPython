# Faktöriyel hesaplama

sayi = int(input("Faktöriyeli hesaplanacak sayı: "))
faktoriyel = 1

for i in range(1, sayi+1, 1):
    faktoriyel *= i
print(faktoriyel)
