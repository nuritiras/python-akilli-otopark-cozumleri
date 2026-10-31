# 4. Uygulama: Mantıksal operatörler

park_suresi = float(input("Park süresini saat olarak giriniz: "))

print("1 - Öğrenci")
print("2 - Öğretmen")
print("3 - Diğer")
arac_sahibi = int(input("Araç sahibi kimdir? "))

if park_suresi >= 3 and (arac_sahibi == 1 or arac_sahibi == 2):
    print("İndirim uygulanacaktır.")
else:
    print("İndirim uygulanmayacaktır.")
