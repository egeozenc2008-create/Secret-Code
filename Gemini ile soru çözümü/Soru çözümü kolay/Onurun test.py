# 1. Ham Veri (Immutable - Değişmez kabul ediyoruz)
sinif_listesi = [
    {"isim": "Ahmet", "vize": 40, "final": 60},
    {"isim": "Ayşe",  "vize": 90, "final": 80},
    {"isim": "Mehmet","vize": 30, "final": 40},
    {"isim": "Fatma", "vize": 50, "final": 50}
]

# 2. Saf Fonksiyonlar (Pure Functions - Yan etkisi yok)
# Bu fonksiyonlar dışarıdan bir şeyi değiştirmez, sadece GİRDİ alır ve ÇIKTI verir.

def ortalama_hesapla(ogrenci):
    """Öğrenciyi alır, ortalamasını ekleyip YENİ bir veri döndürür."""
    yeni_veri = ogrenci.copy() # Orijinal veriyi bozmuyoruz!
    yeni_veri["ort"] = (ogrenci["vize"] * 0.4) + (ogrenci["final"] * 0.6)
    return yeni_veri

def gecenleri_sec(ogrenci):
    """Sadece geçenleri filtrelemek için mantık."""
    return ogrenci["ort"] >= 50

# 3. Boru Hattı (The Pipeline)
# Veriyi al -> İşle -> Filtrele -> Listeye Çevir
# map: Dönüştürür | filter: Süzer

sonuc_listesi = list(
    filter(gecenleri_sec, map(ortalama_hesapla, sinif_listesi))
)

# Çıktıyı Göster (Yan Etki sadece burada yapılır)
print("--- GEÇEN ÖĞRENCİLER LİSTESİ ---")
print(sonuc_listesi)