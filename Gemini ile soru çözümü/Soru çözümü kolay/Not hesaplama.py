# Kullanıcıdan verileri al (input her zaman string döner, int veya float'a çevirmelisin)
vize1 = float(input("1. Vize notunu giriniz: "))
vize2 = float(input("2. Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

# Ağırlıklı ortalama hesabı
ortalama = (vize1 * 0.20) + (vize2 * 0.20) + (final * 0.60)

print(f"Ortalamanız: {ortalama}")

# Mantıksal Operatörler (and)
if ortalama >= 50 and final >= 50:
    print("Durum: GEÇTİ")
else:
    # Neden kaldığını belirtmek ekstra puan getirir
    if final < 50:
        print("Durum: KALDI (Final notu 50'nin altında)")
    else:
        print("Durum: KALDI (Ortalama yetersiz)")