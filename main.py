import sys
import pyperclip
from encode_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QTransform
from design import Ui_MainWindow
from morse_functions import text_to_morse, morse_to_text, morseaudio
from other_functions import atbash_encrypt, atbash_decrypt
from vigenere_functions import vigenere_encrypt, vigenere_decrypt
import urllib.parse


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

        # Vigenere
        self.vigenere_key = ''
        self.update_variable()
        self.ui.vigenere_key.textChanged.connect(self.update_variable)
        self.encrypting_vigenere()
        self.ui.vigenere_key.textChanged.connect(self.encrypting_vigenere)
        self.ui.vigenere_original.textChanged.connect(self.encrypting_vigenere)
        self.ui.action_vigenere_btn.clicked.connect(self.check_btn_vigenere)
        self.ui.copy_vigenere_btn.clicked.connect(self.copy_text_vigenere)

        # Other
        self.ui.atbash.clicked.connect(lambda: self.choose_type_other(self.encrypt_atbash, self.decrypt_atbash))
        self.ui.hash.clicked.connect(lambda: self.choose_type_other(self.encrypting_hash, self.decrypting_hash))
        self.ui.url.clicked.connect(lambda: self.choose_type_other(self.encrypt_url, self.decrypt_url))
        self.ui.other_action_btn.clicked.connect(self.check_btn_other)
        self.ui.other_copy_btn.clicked.connect(self.copy_text_other)

    def update_variable(self):
        self.vigenere_key = self.ui.vigenere_key.text()
        if len(self.vigenere_key) == 0:
            self.ui.vigenere_original.clear()
            self.ui.vigenere_original.setEnabled(False)
            self.ui.vigenere_enc_dec.clear()
            self.ui.vigenere_enc_dec.setEnabled(False)
        else:
            self.ui.vigenere_original.setEnabled(True)
            self.ui.vigenere_enc_dec.setEnabled(True)

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
        self.ui.other_enc_dec.setText(str(hash(self.ui.other_original.toPlainText())))

    def decrypting_hash(self):
        self.ui.other_enc_dec.setText("Hash невозможно дешифровать.")
    def encrypt_atbash(self):
        self.ui.other_enc_dec.setText(atbash_encrypt(self.ui.other_original.toPlainText()))
    def decrypt_atbash(self):
        self.ui.other_enc_dec.setText(atbash_decrypt(self.ui.other_original.toPlainText()))
    def encrypt_url(self):
        self.ui.other_enc_dec.setText(urllib.parse.quote(self.ui.other_original.toPlainText()))
    def decrypt_url(self):
        self.ui.other_enc_dec.setText(urllib.parse.unquote(self.ui.other_original.toPlainText()))
    def encrypting_vigenere(self):
        self.ui.vigenere_enc_dec.setText(vigenere_encrypt(self.ui.vigenere_original.toPlainText(), self.vigenere_key))
    def decrypting_vigenere(self):
        self.ui.vigenere_enc_dec.setText(vigenere_decrypt(self.ui.vigenere_original.toPlainText(), self.vigenere_key))



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

    def check_btn_vigenere(self):
        if self.ui.action_vigenere_btn.isChecked():
            self.encrypting_vigenere()
            self.ui.action_vigenere_btn.setText("Зашифровать")
            self.ui.vigenere_original.textChanged.connect(self.encrypting_vigenere)
            self.ui.vigenere_key.textChanged.connect(self.encrypting_vigenere)
        else:
            self.decrypting_vigenere()
            self.ui.action_vigenere_btn.setText("Дешифровать")
            self.ui.vigenere_original.textChanged.connect(self.decrypting_vigenere)
            self.ui.vigenere_key.textChanged.connect(self.decrypting_vigenere)

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
    def copy_text_vigenere(self):
        self.copy_text(self.ui.vigenere_enc_dec)
    def copy_text_other(self):
        self.copy_text(self.ui.other_enc_dec)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())