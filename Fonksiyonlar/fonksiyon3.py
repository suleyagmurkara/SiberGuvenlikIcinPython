def hesap_makinesi(sayi1, sayi2, islem):
    if islem == 1:
        sonuc = sayi1 + sayi2
    elif islem == 2:
        sonuc = sayi1 - sayi2
    elif islem == 3:
        sonuc = sayi1 * sayi2
    elif islem == 4:
        sonuc = sayi1 / sayi2
    else:
        sonuc = "Hata"
    return sonuc

print(hesap_makinesi(1,2,1))
