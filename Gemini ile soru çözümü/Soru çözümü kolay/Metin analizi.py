cumle = input("Lütfen cümlenizi giriniz").lower()
sesli_harfler = "aeıioöuü"
sayac = 0
for harf in cumle:
    if harf in sesli_harfler:
        sayac += 1
print(f"Girdiğiniz cümlede {sayac} adet sesli harf var.")





