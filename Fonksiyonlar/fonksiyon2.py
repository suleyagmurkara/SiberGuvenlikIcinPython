def cift_sayilar(sayi):
    liste = []
    for i in range(0, sayi, 1):
        if i % 2 == 0:
            liste.append(i)
    return liste

# print(cift_sayilar(10))
