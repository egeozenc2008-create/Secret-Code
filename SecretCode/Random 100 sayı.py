import random

sayilar = [random.randint(1, 100) for i in range(100)]
print(sayilar)

toplam = 0
for sayı in sayilar:
    toplam += sayı





ortalama = toplam / len(sayilar)

print(f"Toplam: {toplam}, Ortalama: {ortalama}")
en_kucuk = sayilar[0]
en_buyuk = sayilar[0]

for sayi in sayilar:
    if sayi < en_kucuk:
        en_kucuk = sayi
    if sayi > en_buyuk:
        en_buyuk = sayi
print("En küçük sayı:", en_kucuk)
print("En büyük sayı:", en_buyuk)

toplam_fark_ve_karesi = 0
for sayi in sayilar:
    toplam_fark_ve_karesi += (sayi - ortalama) ** 2

standart_sapma = (toplam_fark_ve_karesi / len(sayilar) - 1)
print("Standart Sapma:", standart_sapma)


sayıları_sıralama = sorted(sayilar, reverse=True)
print("Büyükten küçüğe sıralanmış sayılar:", sayıları_sıralama)

sayıları_sıralama2 = sorted(sayilar, reverse= False)
print("Küçükten büyüğe sıralanmış sayılar:",sayıları_sıralama2)