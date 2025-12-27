import json

aranan_isim = input("Notunu öğrenmek istediğiniz ismi girin: ")
bulundu_mu = False

# 1. Dosyayı OKUMA modunda aç
try:
    with open("ogrenciler.json", "r") as f:
        liste = json.load(f)  # Dosyadaki veriyi Python listesine çevirir

        # 2. Liste içinde sözlükleri gez
        for ogrenci in liste:
            if ogrenci["isim"] == aranan_isim:
                print(f"{aranan_isim} adlı öğrencinin notu: {ogrenci['not']}")
                bulundu_mu = True
                break  # Bulunca döngüyü kır, boşuna dönmesin

        if not bulundu_mu:
            print("Böyle bir öğrenci kayıtlarda yok.")

except FileNotFoundError:
    print("Hata: ogrenciler.json dosyasında bulunamadı!")