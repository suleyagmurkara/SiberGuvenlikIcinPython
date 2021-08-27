# Sınıf Kontrol

a_sinifi = ["Ahmet", "Mehmet"]
b_sinifi = ["Ali", "Ayşe"]

isim = input("İsim Giriniz: ")

if isim in a_sinifi:
    print("Kişi A sınıfındadır.")
elif isim in b_sinifi:
    print("Kişi B sınıfındadır.")
else:
    print("Kişi sınıflarda bulunmamaktadır.")
