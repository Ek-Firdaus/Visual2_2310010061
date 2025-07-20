import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class MahasiswaForm(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        try:
            loadUi('mahasiswa.ui', self)
            print("UI berhasil dimuat")
        except Exception as e:
            print("Gagal memuat UI:", e)
        self.setWindowTitle("Form Mahasiswa")

        self.TAMBAH.clicked.connect(self.tambahData)
        self.UBAH.clicked.connect(self.ubahData)
        self.HAPUS.clicked.connect(self.hapusData)
        self.BATAL.clicked.connect(self.batalForm)
        self.tableWidget.cellClicked.connect(self.tampilDataKlik)

        # self.loadData()
        try:
            self.loadData()
        except Exception as e:
            print("Gagal load data awal:", e)

    def koneksi(self):
        return mc.connect(
            host="localhost",
            user="root",
            password="",
            database="db_mahasiswa"
        )

    def tambahData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()

            sql = "INSERT INTO mhs VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (
                self.lineEdit_npm.text(),
                self.lineEdit_nama.text(),
                self.lineEdit_panggilan.text(),
                self.lineEdit_telp.text(),
                self.lineEdit_email.text(),
                self.lineEdit_kelas.text(),
                self.lineEdit_matkul.text(),
                self.lineEdit_lokasi_2.text()
            )

            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal tambah:", e)

    def ubahData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()

            sql = """
                UPDATE mhs SET
                    nama_lengkap=%s,
                    nama_panggilan=%s,
                    telepon=%s,
                    email=%s,
                    kelas=%s,
                    matkul=%s,
                    lokasi_kampus=%s
                WHERE npm=%s
            """
            data = (
                self.lineEdit_nama.text(),
                self.lineEdit_panggilan.text(),
                self.lineEdit_telp.text(),
                self.lineEdit_email.text(),
                self.lineEdit_kelas.text(),
                self.lineEdit_matkul.text(),
                self.lineEdit_lokasi_2.text(),
                self.lineEdit_npm.text()
            )

            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal ubah:", e)

    def hapusData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()

            sql = "DELETE FROM mhs WHERE npm=%s"
            data = (self.lineEdit_npm.text(),)

            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal hapus:", e)

    def loadData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()

            cursor.execute("SELECT * FROM mhs")
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(8)

            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        except Exception as e:
            print("Gagal load data:", e)

    def tampilDataKlik(self, row):
        self.lineEdit_npm.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_nama.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_panggilan.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_telp.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_email.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_kelas.setText(self.tableWidget.item(row, 5).text())
        self.lineEdit_matkul.setText(self.tableWidget.item(row, 6).text())
        self.lineEdit_lokasi_2.setText(self.tableWidget.item(row, 7).text())

    def batalForm(self):
        self.lineEdit_npm.clear()
        self.lineEdit_nama.clear()
        self.lineEdit_panggilan.clear()
        self.lineEdit_telp.clear()
        self.lineEdit_email.clear()
        self.lineEdit_kelas.clear()
        self.lineEdit_matkul.clear()
        self.lineEdit_lokasi_2.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

