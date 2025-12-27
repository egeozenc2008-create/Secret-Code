import json
# Test verisi oluşturuyoruz (Sınavda hoca bunu hazır verebilir)
veri = [{"isim": "Ali", "not": 50}, {"isim": "Ayşe", "not": 90}, {"isim": "Mehmet", "not": 70}]
with open("ogrenciler.json", "w") as f:
    json.dump(veri, f)