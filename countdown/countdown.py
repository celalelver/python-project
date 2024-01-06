import random

sayi = random.randint(1, 100)  # Sayıyı belirliyoruz.
print(sayi)
hak = 5  # Hak sayısını girdik.
while True:
    print("Kalan Hakkınız:", hak)  # Hak sayısını yazdırdık
    tahmin = int(input("1-100 arasındaki tahmininizi giriniz..: "))  # tahmini aldık

    if hak == 1:  # Hak sayısı 1 olunca(Bitince)
        print("Kaybettiniz.", sayi)
        break
    elif tahmin < sayi:  # Tahmin küçükse
        print(tahmin, "sayısından daha BÜYÜK bir sayı giriniz.")
    elif tahmin > sayi:  # Tahmin büyükse
        print(tahmin, "sayısından daha KÜÇÜK bir sayı giriniz.")
    else:  # Büyük ya da Küçük değilse:
        print("Tebrikler, doğru bildiniz! Sayımız =", sayi)
        break  # döngüden çık
    hak -= 1  # Hakkı 1 eksilt