import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class NilaiForm(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("nilai.ui", self)
        self.setWindowTitle("Form Nilai Mahasiswa")

        self.btnTambah.clicked.connect(self.tambahData)
        self.btnUbah.clicked.connect(self.ubahData)
        self.btnHapus.clicked.connect(self.hapusData)
        self.btnBatal.clicked.connect(self.batalForm)
        self.tableWidget.cellClicked.connect(self.tampilKlik)

        self.loadData()

    def koneksi(self):
        return mc.connect(
            host="localhost",
            user="root",
            password="",
            database="db_mahasiswa"
        )

    def loadData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM nilai")
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels([
                "ID", "ID Mahasiswa", "Nilai Harian", "Nilai Tugas", "Nilai UTS", "Nilai UAS"
            ])

            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        except Exception as e:
            print("Gagal load data:", e)

    def tambahData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()
            sql = "INSERT INTO nilai (id_mahasiswa, nilai_harian, nilai_tugas, nilai_uts, nilai_uas) VALUES (%s,%s,%s,%s,%s)"
            data = (
                self.lineEdit_id_mhs.text(),
                self.lineEdit_harian.text(),
                self.lineEdit_tugas.text(),
                self.lineEdit_uts.text(),
                self.lineEdit_uas.text()
            )
            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal tambah data:", e)

    def ubahData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()
            sql = """
                UPDATE nilai SET
                    id_mahasiswa=%s,
                    nilai_harian=%s,
                    nilai_tugas=%s,
                    nilai_uts=%s,
                    nilai_uas=%s
                WHERE id=%s
            """
            data = (
                self.lineEdit_id_mhs.text(),
                self.lineEdit_harian.text(),
                self.lineEdit_tugas.text(),
                self.lineEdit_uts.text(),
                self.lineEdit_uas.text(),
                self.lineEdit_id.text()
            )
            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal ubah data:", e)

    def hapusData(self):
        try:
            db = self.koneksi()
            cursor = db.cursor()
            sql = "DELETE FROM nilai WHERE id=%s"
            data = (self.lineEdit_id.text(),)
            cursor.execute(sql, data)
            db.commit()
            self.loadData()
            self.batalForm()
        except Exception as e:
            print("Gagal hapus data:", e)

    def tampilKlik(self, row):
        self.lineEdit_id.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_id_mhs.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_harian.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_tugas.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_uts.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_uas.setText(self.tableWidget.item(row, 5).text())

    def batalForm(self):
        self.lineEdit_id.clear()
        self.lineEdit_id_mhs.clear()
        self.lineEdit_harian.clear()
        self.lineEdit_tugas.clear()
        self.lineEdit_uts.clear()
        self.lineEdit_uas.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NilaiForm()
    window.show()
    sys.exit(app.exec_())