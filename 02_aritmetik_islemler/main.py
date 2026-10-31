# 2. Uygulama: Veri türü dönüşümü ve aritmetik işlemler

park_suresi = float(input("Kaç saat park edeceksiniz? "))

saatlik_ucret = 50
hizmet_bedeli = 10

toplam_ucret = park_suresi * saatlik_ucret
son_ucret = toplam_ucret + hizmet_bedeli

print("Park Ücreti:", toplam_ucret, "TL")
print("Hizmet Bedeli:", hizmet_bedeli, "TL")
print("Ödenecek Toplam Tutar:", son_ucret, "TL")
