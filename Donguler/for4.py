# String ifadedeki karakter ve rakam sayısını bulma

veri = "Eğitim 101"
egitim = list(veri)
print(egitim)

karakter_sayici = 0
rakam_sayici = 0

for i in egitim:
    if str(i).isdecimal():
        rakam_sayici += 1
    else:
        karakter_sayici += 1

print("Karakter sayısı: ", karakter_sayici)
print("Rakam sayısı: ", rakam_sayici)
