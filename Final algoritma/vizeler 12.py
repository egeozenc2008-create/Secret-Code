import os
import json

def dizin_yapisini_getir(kok_dizin):
    klasor_adi = os.path.basename(kok_dizin)
    if not klasor_adi:
        klasor_adi = kok_dizin

    yapi = {
        "klasor_adi": klasor_adi,
        "yol": kok_dizin,
        "dosyalar": [],
        "alt_klasorler": []
    }

    with os.scandir(kok_dizin) as girdiler:
        for girdi in girdiler:
            if girdi.is_file():
                yapi["dosyalar"].append(girdi.name)
            elif girdi.is_dir():
                yapi["alt_klasorler"].append(dizin_yapisini_getir(girdi.path)) #Dikkat et
    return yapi

# ---------------------------------------------------------
# BURAYI DÜZENLE: Taramak istediğin klasörün yolunu tırnak içine yaz
hedef_dizin = r"C:\Users\MONSTER\Desktop\Vİzeler algoritma çalışma"
# Veya Windows kullanıyorsan: r"C:\Kullanicilar\Sen\Masaustu"
# ---------------------------------------------------------

cikti_dosyasi = "dosya_yapisi.json"

print(f"Dizin taranıyor: {hedef_dizin}...")
dosya_verisi = dizin_yapisini_getir(hedef_dizin)

print("JSON dosyası kaydediliyor...")
with open(cikti_dosyasi, 'w' ) as json_dosyasi:
    json.dump(dosya_verisi, json_dosyasi, indent=4)

print(f"İşlem tamam! Veriler '{cikti_dosyasi}' dosyasına kaydedildi.")