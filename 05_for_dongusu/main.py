# 5. Uygulama: for döngüsü ve sayaç kullanımı

uzun_sureli_arac = 0

for i in range(1, 6):
    park_suresi = float(
        input(str(i) + ". aracın park süresini giriniz: ")
    )

    print("Park süresi:", park_suresi, "saat")

    if park_suresi > 3:
        uzun_sureli_arac += 1

print("3 saatten fazla kalan araç sayısı:", uzun_sureli_arac)
