# 8. Uygulama: Qt Designer ve PyQt6 ile otopark ücret hesaplama

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Otopark(QMainWindow):
    def __init__(self):
        super().__init__()

        # Qt Designer ile oluşturulan arayüzü yükle
        uic.loadUi("otopark.ui", self)

        # Butonun tıklanma olayını fonksiyona bağla
        self.pushButton.clicked.connect(self.ucret_hesapla)

    def ucret_hesapla(self):
        try:
            park_suresi = float(self.lineEdit.text())

            if park_suresi <= 0:
                raise ValueError

            saatlik_ucret = 50
            toplam_ucret = park_suresi * saatlik_ucret

            if park_suresi > 2:
                toplam_ucret = toplam_ucret * 0.90

            self.label.setText(
                f"Ödenecek Ücret: {toplam_ucret:.2f} TL"
            )

        except ValueError:
            self.label.setText("Lütfen sıfırdan büyük geçerli bir süre giriniz.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Otopark()
    pencere.show()
    sys.exit(app.exec())
