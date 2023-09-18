import sys
import pyperclip
from encode_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QTransform
from design import Ui_MainWindow
from morse_functions import text_to_morse, morse_to_text, morseaudio


class RotDecoder(QMainWindow):
    def __init__(self):
        super(RotDecoder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Caesar
        self.connection_slider_spinbox()
        self.encrypting_caesar()
        self.ui.spinBox.valueChanged.connect(self.encrypting_caesar)
        self.ui.textEdit.textChanged.connect(self.encrypting_caesar)
        self.ui.actio.clicked.connect(self.check_btn_caesar)
        self.ui.copy_caesar_btn.clicked.connect(self.copy_text_caesar)

        # Morse
        self.encrypting_morse()
        self.ui.morse_original.textChanged.connect(self.encrypting_morse)
        self.ui.morse_action_btn.clicked.connect(self.check_btn_morse)
        self.ui.morse_sound_btn.clicked.connect(self.audiomorse)
        self.ui.copy_morse_btn.clicked.connect(self.copy_text_morse)

        # Disk
        self.key = QPixmap("images/key.png")
        self.outer_wheel = QPixmap("images/outer_wheel.png")
        self.ui.key_slider.valueChanged.connect(self.rotate_key)
        self.ui.wheel_slider.valueChanged.connect(self.rotate_wheel)

        # Other
        self.ui.hash.clicked.connect(lambda: self.choose_type_other(self.encrypting_hash, self.decrypting_hash))
        self.ui.other_action_btn.clicked.connect(self.check_btn_other)
        self.ui.other_copy_btn.clicked.connect(self.copy_text_other)

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

    # Encrypting/Decrypting Functions
    def encrypting_caesar(self):
        self.ui.textEdit_2.setText(encrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value()))

    def decrypting_caesar(self):
        self.ui.textEdit_2.setText(decrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value())[0])

    def encrypting_morse(self):
        self.ui.morse_enc_dec.setText(text_to_morse(self.ui.morse_original.toPlainText()))

    def decrypting_morse(self):
        self.ui.morse_enc_dec.setText(morse_to_text(self.ui.morse_original.toPlainText()))

    def encrypting_hash(self):
        print("Я шифрую")
        self.ui.other_enc_dec.setText(str(hash(self.ui.other_original.toPlainText())))

    def decrypting_hash(self):
        print("Я дешифрую")
        self.ui.other_enc_dec.setText("Hash невозможно дешифровать.")

    def check_btn_caesar(self):
        if self.ui.actio.isChecked():
            self.encrypting_caesar()
            self.ui.actio.setText("Зашифровать")
            self.ui.spinBox.valueChanged.connect(self.encrypting_caesar)
            self.ui.textEdit.textChanged.connect(self.encrypting_caesar)
        else:
            self.decrypting_caesar()
            self.ui.actio.setText("Дешифровать")
            self.ui.spinBox.valueChanged.connect(self.decrypting_caesar)
            self.ui.textEdit.textChanged.connect(self.decrypting_caesar)

    def check_btn_morse(self):
        if self.ui.morse_action_btn.isChecked():
            self.encrypting_morse()
            self.ui.morse_action_btn.setText("Зашифровать")
            self.ui.morse_original.textChanged.connect(self.encrypting_morse)
            self.ui.morse_sound_btn.setEnabled(True)
        else:
            self.decrypting_morse()
            self.ui.morse_action_btn.setText("Дешифровать")
            self.ui.morse_original.textChanged.connect(self.decrypting_morse)
            self.ui.morse_sound_btn.setEnabled(False)

    def check_btn_other(self):
        if self.ui.other_action_btn.isChecked():
            self.ui.other_action_btn.setText("Зашифровать")
        else:
            self.ui.other_action_btn.setText("Дешифровать")

    def choose_type_other(self, enc_func, dec_func):
        if self.ui.other_action_btn.isChecked():
            enc_func()
        else:
            dec_func()

    def audiomorse(self):
        morseaudio(self.ui.morse_enc_dec.toPlainText())

    # Copy Text Functions
    def copy_text(self, textField):
        pyperclip.copy(textField.toPlainText())

    def copy_text_caesar(self):
        self.copy_text(self.ui.textEdit_2)
    def copy_text_morse(self):
        self.copy_text(self.ui.morse_enc_dec)
    def copy_text_other(self):
        self.copy_text(self.ui.other_enc_dec)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())