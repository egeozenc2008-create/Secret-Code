# 1. Liste Oluşturma
# 0'dan 99'a kadar (toplam 100) sayı içeren bir liste oluştururuz.
liste_sayilar = list(range(100))
print("Oluşturulan liste:",
      liste_sayilar)  # Listenin tamamını yazdırmak yerine, ilk ve son elemanları kontrol edebiliriz.
print(f"Liste boyutu: {len(liste_sayilar)}")

# 2. Toplam ve Ortalama Hesaplama
# Python'ın yerleşik (built-in) fonksiyonları olan sum() ve len() ile pratikçe hesaplayabiliriz.
liste_toplam = sum(liste_sayilar)
# Ortalamayı bulmak için toplamı eleman sayısına böleriz.
liste_ortalama = liste_toplam / len(liste_sayilar)

print(f"\nListenin Toplamı: {liste_toplam}")
print(f"Listenin Ortalaması: {liste_ortalama}")

# 3. En Büyük ve En Küçük Değerleri Bulma (Döngü Kullanarak)
# Fonksiyon kullanmak yerine, bu işlemi listenin üzerinde doğrudan döngü kurarak yapalım.

# Listenin ilk elemanını başlangıç değeri olarak atıyoruz.
en_kucuk = liste_sayilar[0]
en_buyuk = liste_sayilar[0]

# Listenin her elemanını tek tek kontrol ediyoruz.
for sayi in liste_sayilar:
    # Karşılaştırma yaparak en küçük ve en büyük değerleri bulma
    if sayi < en_kucuk:
        en_kucuk = sayi

    if sayi > en_buyuk:
        en_buyuk = sayi

# 4. Sonuçları Yazdırma
print(f"\nDöngü ile bulunan En Büyük Değer: {en_buyuk}")
print(f"Döngü ile bulunan En Küçük Değer: {en_kucuk}")

# Not: Python'da pratik yol, max() ve min() kullanmaktır:
# print(f"Pratik En Büyük: {max(liste_sayilar)}")
# print(f"Pratik En Küçük: {min(liste_sayilar)}")