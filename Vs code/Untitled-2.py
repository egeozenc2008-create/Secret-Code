def hesapla(ifade):
    try:
        # Sadece izin verilen karakterler var mı kontrol et
        izinli_karakterler = "0123456789+-*/(). "
        if any(char not in izinli_karakterler for char in ifade):
            return "Geçersiz karakter kullandınız!"

        # İfadeyi hesapla
        sonuc = eval(ifade)
        return sonuc
    except ZeroDivisionError:
        return "Sıfıra bölme hatası!"
    except Exception as e:
        return f"Hata: {str(e)}"

# Ana döngü
while True:
    ifade = input("İşlemi girin (örn: 2+3*4) - çıkmak için 'çık' yazın: ").strip()
    if ifade.lower() == "çık":
        print("Hesap makinesi kapatılıyor...")
        break
    print("Sonuç:", hesapla(ifade))





