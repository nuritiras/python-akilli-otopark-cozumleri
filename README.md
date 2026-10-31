# Python Uygulama Sınavı – Çözümlü Çalışma Rehberi
## Yapay Zekâ Destekli Akıllı Otopark Yönetim Sistemi

**Ders:** Nesne Tabanlı Programlama  
**Alan:** Bilişim Teknolojileri – Yazılım Geliştirme  
**Sınıf:** 10. Sınıf  
**Programlama dili:** Python  
**Arayüz:** Qt Designer ve PyQt6

Bu depo, Python uygulama sınavına hazırlık amacıyla hazırlanmıştır. Sekiz uygulamanın çözüm kodlarını içerir.

## Klasör yapısı

```text
python-akilli-otopark-cozumleri/
├── README.md
├── 01_degiskenler/
│   └── main.py
├── 02_aritmetik_islemler/
│   └── main.py
├── 03_kosul_yapilari/
│   └── main.py
├── 04_mantiksal_operatorler/
│   └── main.py
├── 05_for_dongusu/
│   └── main.py
├── 06_while_break_continue/
│   └── main.py
├── 07_hata_yonetimi/
│   └── main.py
└── 08_qt_designer_pyqt6/
    ├── main.py
    └── otopark.ui
```

## Uygulamaları çalıştırma

Python 3 kurulu olmalıdır. Terminali ilgili klasörde açıp örneğin:

```bash
python3 main.py
```

komutunu çalıştırabilirsiniz.

Qt Designer ve PyQt6 uygulaması için önce:

```bash
pip install PyQt6
```

komutuyla PyQt6 paketini yükleyiniz. Ardından `08_qt_designer_pyqt6` klasöründe:

```bash
python3 main.py
```

komutunu çalıştırınız.

`main.py` ile `otopark.ui` aynı klasörde bulunmalıdır.

## Uygulama konuları

| No | Konu |
|---|---|
| 1 | Değişkenler ve temel veri türleri |
| 2 | Veri türü dönüşümü ve aritmetik işlemler |
| 3 | Karşılaştırma ve koşul yapıları |
| 4 | Mantıksal operatörler |
| 5 | `for` döngüsü ve sayaç |
| 6 | `while`, `break` ve `continue` |
| 7 | Hata yönetimi ve kural tabanlı karar desteği |
| 8 | Qt Designer ve PyQt6 ile masaüstü arayüzü |

## Öğrenme notu

Kodları doğrudan kopyalamak yerine önce ilgili soruyu kendiniz çözmeye çalışınız. Daha sonra çözümle karşılaştırıp farklı giriş değerleriyle test ediniz.

**Not:** 7. uygulamadaki doluluk oranına göre öneri üretme yaklaşımı, kural tabanlı basit bir karar destek örneğidir; öğrenen bir makine öğrenmesi modeli değildir.
