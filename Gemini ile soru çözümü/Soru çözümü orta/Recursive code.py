def ters_cevir(yazı):
    if len(yazı) == 0:
        return ""

    return yazı[-1] + ters_cevir(yazı[:-1])

kelime = input("Ters çevirmek istediğiniz kelimeyi giriniz:")
sonuc = ters_cevir(kelime)

print(sonuc)

