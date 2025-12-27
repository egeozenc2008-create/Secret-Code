import os

sayac = 0  # Toplam sayıyı tutmak için global değişken (veya fonksiyona return ettirebilirsin)


def txt_sayaci(yol):
    global sayac  # Dışarıdaki sayacı değiştirmek için

    try:
        dosyalar = os.listdir(yol)
    except PermissionError:
        return  # İzin yoksa girme

    for dosya in dosyalar:
        tam_yol = os.path.join(yol, dosya)

        if os.path.isfile(tam_yol):
            # Dosya isminin sonu .txt ile bitiyor mu?
            if dosya.endswith(".txt"):
                print(f"Bulundu: {dosya}")
                sayac += 1

        elif os.path.isdir(tam_yol):
            txt_sayaci(tam_yol)  # Recursion (Alt klasöre dal)


klasor = r"C:\Users\MONSTER\Desktop\Vİzeler algoritma çalışma"  # Kendi yolunu yaz
txt_sayaci(klasor)
print(f"\nToplam {sayac} adet .txt dosyası bulundu.")
