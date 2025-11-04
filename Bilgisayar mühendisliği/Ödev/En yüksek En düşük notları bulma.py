notlar = [85, 92, 45, 78, 99, 60, 95]

en_küçük = notlar[0]
en_büyük = notlar[0]
for not_değeri in notlar:

    if not_değeri < en_küçük:
        en_küçük = not_değeri

    if not_değeri > en_büyük:
        en_büyük = not_değeri


print("Not liste:", notlar)
print("En küçük değeri:",en_küçük)
print("En büyük değeri:",en_büyük)
