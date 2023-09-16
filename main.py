import sys
from encode_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView
from PySide6.QtGui import QPixmap, QTransform
from design import Ui_MainWindow


class RotDecoder(QMainWindow):
    def __init__(self):
        super(RotDecoder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Caesar
        self.connection_slider_spinbox()
        self.encrypting()
        self.ui.spinBox.valueChanged.connect(self.encrypting)
        self.ui.textEdit.textChanged.connect(self.encrypting)
        self.ui.actio.clicked.connect(self.checked_enc_dec_btn)
        # Disk
        self.key = QPixmap("images/key.png")
        self.outer_wheel = QPixmap("images/outer_wheel.png")
        self.ui.key_slider.valueChanged.connect(self.rotate_key)
        self.ui.wheel_slider.valueChanged.connect(self.rotate_wheel)

    def rotate_wheel(self):
        self.transform = QTransform().rotate(self.ui.wheel_slider.sliderPosition())
        self.rotated_image = self.outer_wheel.transformed(self.transform)
        self.ui.outer_wheel.setPixmap(self.rotated_image)
    def rotate_key(self):
        self.transform = QTransform().rotate(self.ui.key_slider.sliderPosition())
        self.rotated_image = self.key.transformed(self.transform)
        self.ui.key.setPixmap(self.rotated_image)
    def connection_slider_spinbox(self) -> None:
        self.ui.horizontalSlider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.horizontalSlider.setValue)

    def decrypting(self):
        self.ui.textEdit_2.setText(decrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value())[0])

    def checked_enc_dec_btn(self):
        if self.ui.actio.isChecked():
            self.encrypting()
            self.ui.actio.setText("Зашифровать")
            self.ui.spinBox.valueChanged.connect(self.encrypting)
            self.ui.textEdit.textChanged.connect(self.encrypting)
        else:
            self.decrypting()
            self.ui.actio.setText("Дешифровать")
            self.ui.spinBox.valueChanged.connect(self.decrypting)
            self.ui.textEdit.textChanged.connect(self.decrypting)
    def encrypting(self):
        self.ui.textEdit_2.setText(encrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value()))
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())