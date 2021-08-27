# Hesap Makinesi

print("Toplama = 1 \n"
      "Çıkarma = 2 \n"
      "Çarpma  = 3 \n"
      "Bölme   = 4")
islem = input("İşlemi Seçiniz: ")
sayi1 = int(input("Sayi 1: "))
sayi2 = int(input("Sayi 2: "))

if islem == "1":
    sonuc = int(sayi1) + int(sayi2)
    print("Sonuç: ", str(sonuc))
elif islem == "2":
    sonuc = int(sayi1) - int(sayi2)
    print("Sonuç: ", str(sonuc))
elif islem == "3":
    sonuc = int(sayi1) * int(sayi2)
    print("Sonuç: ", str(sonuc))
elif islem == "4":
    if sayi2 > 0:
        sonuc = int(sayi1) / int(sayi2)
        print("Sonuç: ", str(sonuc))
    elif sayi2 == 0:
        print("!!!Sayi 2 = 0(sıfır) olamaz!!!")
else:
    print("!!!Hatalı işlem seçimi!!!")
