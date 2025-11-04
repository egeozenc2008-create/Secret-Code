sayı = int(input("Lütfen faktoriyeli hesaplamak için bir sayı giriniz:"))
faktoriyel = 1
if sayı <= 0:
    print("Negatif sayı girmeyiniz")
elif sayı == 0:
    print("0! = 1 ")
else:
    for i in range(1, sayı+1):
        faktoriyel *= i
        print(f"{sayı}'nin faktöriyeli ({sayı}!):", faktoriyel)