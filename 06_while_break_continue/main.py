# 6. Uygulama: while, break ve continue

arac_sayisi = 0

while True:
    plaka = input("Araç plakasını giriniz (Çıkış: BİTİR): ")

    if plaka == "BİTİR":
        break

    if plaka == "":
        print("Plaka boş bırakılamaz.")
        continue

    print("Araç kaydedildi.")
    arac_sayisi += 1

print("Toplam kayıtlı araç sayısı:", arac_sayisi)
