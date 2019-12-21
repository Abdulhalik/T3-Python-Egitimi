# coding=utf-8
from Orta import ortalama  # Orta kütüphanesinden metot import ettik

myList = []
deger = int(input("Ogrenci adeti giriniz: "))

while deger != 0:
    notlar = int(input("not giriniz: "))
    myList.append(notlar)
    deger = deger - 1

print("ortalama: ", ortalama(myList))