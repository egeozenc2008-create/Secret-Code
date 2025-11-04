toplam_while = 0
sayac = 0  # Saymaya 0'dan başlıyoruz

while sayac <= 100:  # Sayaç 100 olana kadar (100 dahil) devam et
    toplam_while = toplam_while + sayac
    sayac = sayac + 1  # Sayaçı birer birer artır (sayac += 1 şeklinde de yazılabilir)

print("while döngüsü ile 0'dan 100'e kadar olan sayıların toplamı:", toplam_while)