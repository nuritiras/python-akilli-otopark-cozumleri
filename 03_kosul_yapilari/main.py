# 3. Uygulama: Karşılaştırma ve koşul yapıları

dolu_arac = int(input("Dolu araç sayısını giriniz: "))

if dolu_arac < 0:
    print("Geçersiz araç sayısı")
elif dolu_arac >= 100:
    print("Otopark DOLU")
elif dolu_arac >= 80:
    print("Otoparkta az sayıda yer kaldı")
elif dolu_arac >= 50:
    print("Otoparkta yeterli yer var")
else:
    print("Otoparkta çok sayıda boş yer var")
