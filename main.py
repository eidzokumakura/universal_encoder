import sys
from encode_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from design import Ui_MainWindow


class RotDecoder(QMainWindow):
    def __init__(self):
        super(RotDecoder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection_slider_spinbox()

    def connection_slider_spinbox(self) -> None:
        self.ui.horizontalSlider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.horizontalSlider.setValue)

    def decrypting(self):
        self.ui.textEdit_2.setText(decrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value())[0])

    def encrypting(self):
        self.ui.textEdit_2.setText(encrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value()))
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())