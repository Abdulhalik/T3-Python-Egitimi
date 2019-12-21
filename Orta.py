def ortalama(mList):
    toplam = 0
    sonuc = 0
    for x in mList:
        toplam = toplam + x

    sonuc = float(toplam) / len(mList)
    print(sonuc)