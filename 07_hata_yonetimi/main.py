# 7. Uygulama: Hata yönetimi ve kural tabanlı karar destek sistemi

try:
    toplam_kapasite = int(
        input("Otoparkın toplam kapasitesini giriniz: ")
    )
    dolu_arac = int(
        input("Dolu park alanı sayısını giriniz: ")
    )

    if toplam_kapasite <= 0:
        raise ValueError("Toplam kapasite sıfırdan büyük olmalıdır.")

    if dolu_arac < 0 or dolu_arac > toplam_kapasite:
        raise ValueError("Dolu araç sayısı geçersizdir.")

    doluluk_orani = (dolu_arac / toplam_kapasite) * 100
    assert 0 <= doluluk_orani <= 100

except ValueError as hata:
    print("Hata:", hata)

except AssertionError:
    print("Doluluk oranı geçersizdir.")

else:
    print("Doluluk oranı:", doluluk_orani, "%")

    if doluluk_orani >= 90:
        print("Otopark dolmak üzere. Alternatif otopark arayınız.")
    elif doluluk_orani >= 50:
        print("Otoparkta uygun yerler bulunmaktadır.")
    else:
        print("Otoparkta çok sayıda boş yer bulunmaktadır.")

finally:
    print("Otopark kontrol işlemi tamamlandı.")
