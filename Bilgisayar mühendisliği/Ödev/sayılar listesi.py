sayılar_listesi = [15, 20 , 5 , 45 , 10]
liste_toplam = 0
eleman_sayısı = 0
for sayı in sayılar_listesi:
    liste_toplam += sayı
    eleman_sayısı += 1


ortalama = liste_toplam / eleman_sayısı
print("Listedeki sayılar:", sayılar_listesi)
print("Sayıların toplamı:", liste_toplam)
print("Listenin eleman sayısı:", eleman_sayısı)
print("Ortalama:", ortalama)


pratik_ortalama = sum(sayılar_listesi) / len(sayılar_listesi)
print("Pratik ortalama:", pratik_ortalama)










