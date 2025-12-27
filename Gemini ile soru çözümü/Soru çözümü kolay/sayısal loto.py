import random
def loto_cekilisi():
    loto_sayıları = []
    while len(loto_sayıları) < 6:
        sayı = random.randint(1,49)
        if sayı not in loto_sayıları:
            loto_sayıları.append(sayı)



    loto_sayıları.sort()
    print("Bu haftanın şanslı sayısı:",loto_sayıları)

loto_cekilisi()



