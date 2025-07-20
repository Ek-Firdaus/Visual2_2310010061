import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


from mahasiswa import MahasiswaForm
from nilai import NilaiForm

class MenuUtama(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("menu.ui", self)
        self.setWindowTitle("Menu Mahasiswa")

        self.btnMahasiswa.clicked.connect(self.bukaFormMahasiswa)
        self.btnNilai.clicked.connect(self.bukaFormNilai)

    def bukaFormMahasiswa(self):
        self.mahasiswa_form = MahasiswaForm()
        self.mahasiswa_form.show()

    def bukaFormNilai(self):
        self.nilai_form = NilaiForm()
        self.nilai_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuUtama()
    window.show()
    sys.exit(app.exec_())
