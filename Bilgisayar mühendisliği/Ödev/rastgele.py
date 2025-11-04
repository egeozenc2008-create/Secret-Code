metin = "Python ile vizeye hazirlaniyorum"
sesli_harfler = "aeiouAEIOU"  # Kontrol edeceğimiz sesli harfler
sesli_sayisi = 0

# Metin içindeki her bir karakteri tek tek kontrol et
for karakter in metin:
    # Karakterin sesli_harfler string'i içinde olup olmadığını kontrol et
    # "in" operatörü, bir öğenin bir dizide (liste/string) olup olmadığını kontrol eder.
    if karakter in sesli_harfler:
        sesli_sayisi += 1

print("Kontrol edilen metin:", metin)
print("Toplam sesli harf sayısı:", sesli_sayisi)