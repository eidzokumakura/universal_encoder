# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(790, 706)
        icon = QIcon()
        icon.addFile(u":/images/images/padlock_locked.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.caesar = QWidget()
        self.caesar.setObjectName(u"caesar")
        self.caesar.setStyleSheet(u"QTextEdit {\n"
"	font: 12pt \"Bookman Old Style\";\n"
"	background: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font: 700 12pt \"Bookman Old Style\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #a01914;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #a01914;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    color: white;\n"
"    background-color: #a01914;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #a01914;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: gray;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: black;\n"
"    width: 16px;\n"
"    border-radius:8px;\n"
"    margin-top: -5px;\n"
"    margin-bottom: -5px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 7px;\n"
"}\n"
"QLabel"
                        " {\n"
"    font: 500 11pt \"Bookman Old Style\";\n"
"}\n"
"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"	font: 11pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #009900;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.caesar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.original_text = QVBoxLayout()
        self.original_text.setObjectName(u"original_text")
        self.label = QLabel(self.caesar)
        self.label.setObjectName(u"label")

        self.original_text.addWidget(self.label)

        self.textEdit = QTextEdit(self.caesar)
        self.textEdit.setObjectName(u"textEdit")

        self.original_text.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.original_text)

        self.encrypted_decrypted_text = QVBoxLayout()
        self.encrypted_decrypted_text.setObjectName(u"encrypted_decrypted_text")
        self.label_2 = QLabel(self.caesar)
        self.label_2.setObjectName(u"label_2")

        self.encrypted_decrypted_text.addWidget(self.label_2)

        self.textEdit_2 = QTextEdit(self.caesar)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.encrypted_decrypted_text.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.encrypted_decrypted_text)

        self.buttons = QHBoxLayout()
        self.buttons.setObjectName(u"buttons")
        self.actio = QPushButton(self.caesar)
        self.actio.setObjectName(u"actio")
        self.actio.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/images/padlock_unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/padlock_locked.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/images/images/padlock_unlocked.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon1.addFile(u":/images/images/padlock_locked.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.actio.setIcon(icon1)
        self.actio.setCheckable(True)
        self.actio.setChecked(True)

        self.buttons.addWidget(self.actio)

        self.copy_caesar_btn = QPushButton(self.caesar)
        self.copy_caesar_btn.setObjectName(u"copy_caesar_btn")

        self.buttons.addWidget(self.copy_caesar_btn)


        self.verticalLayout.addLayout(self.buttons)

        self.slider = QHBoxLayout()
        self.slider.setObjectName(u"slider")
        self.label_3 = QLabel(self.caesar)
        self.label_3.setObjectName(u"label_3")

        self.slider.addWidget(self.label_3)

        self.horizontalSlider = QSlider(self.caesar)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.slider.addWidget(self.horizontalSlider)

        self.spinBox = QSpinBox(self.caesar)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(True)
        self.spinBox.setMouseTracking(False)
        self.spinBox.setTabletTracking(False)
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(-50)
        self.spinBox.setMaximum(50)
        self.spinBox.setValue(1)

        self.slider.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.slider)

        self.tabWidget.addTab(self.caesar, "")
        self.morse = QWidget()
        self.morse.setObjectName(u"morse")
        self.morse.setStyleSheet(u"QTextEdit {\n"
"	background: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	font: 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font: 700 12pt \"Bookman Old Style\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #090;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    color: white;\n"
"    background-color: #090;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel {\n"
"    font: 500 11pt \"Bookman Old Style\";\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.morse)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.morse)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.morse_original = QTextEdit(self.morse)
        self.morse_original.setObjectName(u"morse_original")

        self.verticalLayout_3.addWidget(self.morse_original)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.morse)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.morse_enc_dec = QTextEdit(self.morse)
        self.morse_enc_dec.setObjectName(u"morse_enc_dec")

        self.verticalLayout_5.addWidget(self.morse_enc_dec)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.morse_action_btn = QPushButton(self.morse)
        self.morse_action_btn.setObjectName(u"morse_action_btn")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/padlock_unlocked.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/images/padlock_locked.svg", QSize(), QIcon.Normal, QIcon.On)
        self.morse_action_btn.setIcon(icon2)
        self.morse_action_btn.setCheckable(True)
        self.morse_action_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.morse_action_btn)

        self.morse_sound_btn = QPushButton(self.morse)
        self.morse_sound_btn.setObjectName(u"morse_sound_btn")
        self.morse_sound_btn.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/images/images/audio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.morse_sound_btn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.morse_sound_btn)

        self.copy_morse_btn = QPushButton(self.morse)
        self.copy_morse_btn.setObjectName(u"copy_morse_btn")

        self.horizontalLayout.addWidget(self.copy_morse_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.morse, "")
        self.disk = QWidget()
        self.disk.setObjectName(u"disk")
        self.disk.setStyleSheet(u"QSlider::sub-page:horizontal {\n"
"    background-color: #c4b3a1;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: #cab9b0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #b88c47;\n"
"    width: 16px;\n"
"    margin-top: -10px;\n"
"    margin-bottom: -10px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 10px;\n"
"}\n"
"QLabel {\n"
"    font: 500 18pt \"Bookman Old Style\";\n"
"}")
        self.verticalLayoutWidget = QWidget(self.disk)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 460, 771, 71))
        self.wheel_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.wheel_layout.setObjectName(u"wheel_layout")
        self.wheel_layout.setContentsMargins(0, 0, 0, 0)
        self.wheel_label = QLabel(self.verticalLayoutWidget)
        self.wheel_label.setObjectName(u"wheel_label")
        self.wheel_label.setAlignment(Qt.AlignCenter)

        self.wheel_layout.addWidget(self.wheel_label)

        self.wheel_slider = QSlider(self.verticalLayoutWidget)
        self.wheel_slider.setObjectName(u"wheel_slider")
        self.wheel_slider.setMaximum(360)
        self.wheel_slider.setOrientation(Qt.Horizontal)

        self.wheel_layout.addWidget(self.wheel_slider)

        self.verticalLayoutWidget_2 = QWidget(self.disk)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 540, 771, 61))
        self.key_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.key_layout.setObjectName(u"key_layout")
        self.key_layout.setContentsMargins(0, 0, 0, 0)
        self.key_label = QLabel(self.verticalLayoutWidget_2)
        self.key_label.setObjectName(u"key_label")
        self.key_label.setAlignment(Qt.AlignCenter)

        self.key_layout.addWidget(self.key_label)

        self.key_slider = QSlider(self.verticalLayoutWidget_2)
        self.key_slider.setObjectName(u"key_slider")
        self.key_slider.setMaximum(360)
        self.key_slider.setOrientation(Qt.Horizontal)

        self.key_layout.addWidget(self.key_slider)

        self.inner_wheel = QLabel(self.disk)
        self.inner_wheel.setObjectName(u"inner_wheel")
        self.inner_wheel.setGeometry(QRect(0, 0, 771, 491))
        self.inner_wheel.setPixmap(QPixmap(u":/images/images/inner_wheel.png"))
        self.inner_wheel.setAlignment(Qt.AlignCenter)
        self.outer_wheel = QLabel(self.disk)
        self.outer_wheel.setObjectName(u"outer_wheel")
        self.outer_wheel.setGeometry(QRect(0, 0, 771, 491))
        self.outer_wheel.setPixmap(QPixmap(u":/images/images/outer_wheel.png"))
        self.outer_wheel.setAlignment(Qt.AlignCenter)
        self.key = QLabel(self.disk)
        self.key.setObjectName(u"key")
        self.key.setGeometry(QRect(0, 0, 771, 491))
        self.key.setPixmap(QPixmap(u":/images/images/key.png"))
        self.key.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.disk, "")
        self.vigenere = QWidget()
        self.vigenere.setObjectName(u"vigenere")
        self.vigenere.setStyleSheet(u"QTextEdit {\n"
"	background: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	font: 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit {\n"
" background: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	font: 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font: 700 12pt \"Bookman Old Style\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #106ec7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #106ec7;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    color: white;\n"
"    background-color: #106ec7;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel {\n"
"    font: 500 11pt \"Bookman Old Style\";\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.vigenere)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.original_text_2 = QVBoxLayout()
        self.original_text_2.setObjectName(u"original_text_2")
        self.label_13 = QLabel(self.vigenere)
        self.label_13.setObjectName(u"label_13")

        self.original_text_2.addWidget(self.label_13)

        self.vigenere_original = QTextEdit(self.vigenere)
        self.vigenere_original.setObjectName(u"vigenere_original")
        self.vigenere_original.setEnabled(True)

        self.original_text_2.addWidget(self.vigenere_original)


        self.verticalLayout_8.addLayout(self.original_text_2)

        self.encrypted_decrypted_text_2 = QVBoxLayout()
        self.encrypted_decrypted_text_2.setObjectName(u"encrypted_decrypted_text_2")
        self.label_14 = QLabel(self.vigenere)
        self.label_14.setObjectName(u"label_14")

        self.encrypted_decrypted_text_2.addWidget(self.label_14)

        self.vigenere_enc_dec = QTextEdit(self.vigenere)
        self.vigenere_enc_dec.setObjectName(u"vigenere_enc_dec")

        self.encrypted_decrypted_text_2.addWidget(self.vigenere_enc_dec)

        self.key_layout_2 = QHBoxLayout()
        self.key_layout_2.setObjectName(u"key_layout_2")
        self.label_12 = QLabel(self.vigenere)
        self.label_12.setObjectName(u"label_12")

        self.key_layout_2.addWidget(self.label_12)

        self.vigenere_key = QLineEdit(self.vigenere)
        self.vigenere_key.setObjectName(u"vigenere_key")

        self.key_layout_2.addWidget(self.vigenere_key)


        self.encrypted_decrypted_text_2.addLayout(self.key_layout_2)


        self.verticalLayout_8.addLayout(self.encrypted_decrypted_text_2)

        self.buttons_2 = QHBoxLayout()
        self.buttons_2.setObjectName(u"buttons_2")
        self.action_vigenere_btn = QPushButton(self.vigenere)
        self.action_vigenere_btn.setObjectName(u"action_vigenere_btn")
        self.action_vigenere_btn.setEnabled(True)
        self.action_vigenere_btn.setIcon(icon1)
        self.action_vigenere_btn.setCheckable(True)
        self.action_vigenere_btn.setChecked(True)

        self.buttons_2.addWidget(self.action_vigenere_btn)

        self.copy_vigenere_btn = QPushButton(self.vigenere)
        self.copy_vigenere_btn.setObjectName(u"copy_vigenere_btn")

        self.buttons_2.addWidget(self.copy_vigenere_btn)


        self.verticalLayout_8.addLayout(self.buttons_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.vigenere, "")
        self.other = QWidget()
        self.other.setObjectName(u"other")
        self.other.setStyleSheet(u"QTextEdit {\n"
"	background: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	font: 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font: 700 12pt \"Bookman Old Style\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel {\n"
"    font: 500 11pt \"Bookman Old Style\";\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.other)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.other_original_layout = QVBoxLayout()
        self.other_original_layout.setObjectName(u"other_original_layout")
        self.label_6 = QLabel(self.other)
        self.label_6.setObjectName(u"label_6")

        self.other_original_layout.addWidget(self.label_6)

        self.other_original = QTextEdit(self.other)
        self.other_original.setObjectName(u"other_original")

        self.other_original_layout.addWidget(self.other_original)


        self.verticalLayout_9.addLayout(self.other_original_layout)

        self.other_enc_dec_layout = QVBoxLayout()
        self.other_enc_dec_layout.setObjectName(u"other_enc_dec_layout")
        self.label_7 = QLabel(self.other)
        self.label_7.setObjectName(u"label_7")

        self.other_enc_dec_layout.addWidget(self.label_7)

        self.other_enc_dec = QTextEdit(self.other)
        self.other_enc_dec.setObjectName(u"other_enc_dec")

        self.other_enc_dec_layout.addWidget(self.other_enc_dec)


        self.verticalLayout_9.addLayout(self.other_enc_dec_layout)

        self.cipher_btn_vert_layout = QVBoxLayout()
        self.cipher_btn_vert_layout.setObjectName(u"cipher_btn_vert_layout")
        self.main_buttons_layout = QHBoxLayout()
        self.main_buttons_layout.setObjectName(u"main_buttons_layout")
        self.other_action_btn = QPushButton(self.other)
        self.other_action_btn.setObjectName(u"other_action_btn")
        self.other_action_btn.setIcon(icon2)
        self.other_action_btn.setCheckable(True)
        self.other_action_btn.setChecked(True)

        self.main_buttons_layout.addWidget(self.other_action_btn)

        self.other_copy_btn = QPushButton(self.other)
        self.other_copy_btn.setObjectName(u"other_copy_btn")

        self.main_buttons_layout.addWidget(self.other_copy_btn)


        self.cipher_btn_vert_layout.addLayout(self.main_buttons_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hash = QPushButton(self.other)
        self.hash.setObjectName(u"hash")

        self.horizontalLayout_2.addWidget(self.hash)

        self.url = QPushButton(self.other)
        self.url.setObjectName(u"url")

        self.horizontalLayout_2.addWidget(self.url)

        self.atbash = QPushButton(self.other)
        self.atbash.setObjectName(u"atbash")

        self.horizontalLayout_2.addWidget(self.atbash)


        self.cipher_btn_vert_layout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addLayout(self.cipher_btn_vert_layout)

        self.tabWidget.addTab(self.other, "")
        self.about_program = QWidget()
        self.about_program.setObjectName(u"about_program")
        self.about_program.setStyleSheet(u"QLabel {\n"
"	text-align: center;\n"
"	margin: auto;\n"
"	font: 12pt \"Bookman Old Style\";\n"
"}\n"
"QTextBrowser {\n"
"	background: transparent;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.about_program)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textBrowser = QTextBrowser(self.about_program)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamilies([u"Bookman Old Style"])
        self.textBrowser.setFont(font)

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.label_11 = QLabel(self.about_program)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.about_program, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439 \u0448\u0438\u0444\u0440\u0430\u0442\u043e\u0440", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.actio.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.copy_caesar_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caesar), QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.morse_action_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.morse_sound_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438", None))
        self.copy_morse_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.morse), QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0440\u0437\u0435", None))
        self.wheel_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0435\u0441\u043e", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.inner_wheel.setText("")
        self.outer_wheel.setText("")
        self.key.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.disk), QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a\u043e\u0432\u044b\u0439", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f: ", None))
        self.action_vigenere_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.copy_vigenere_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vigenere), QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.other_action_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.other_copy_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.hash.setText(QCoreApplication.translate("MainWindow", u"Hash", None))
        self.url.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.atbash.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0442\u0431\u0430\u0448", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0435", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bookman Old Style'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c"
                        "\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&q"
                        "uot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;/&quot;\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0432\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0428\u0430\u0433 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u0434\u043b\u044f \u0440\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u043a\u0438 \u0448\u0430\u0433\u0430 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f (\u043a\u043b\u044e\u0447\u0430).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:"
                        "700;\">&quot;\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0438 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">\u0428\u0438\u0444\u0440 \u041c\u043e\u0440\u0437\u0435</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d"
                        "\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;/&quot;\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0432\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u0440\u043e\u0441\u043b\u0443"
                        "\u0448\u0430\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 (\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 &quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\""
                        ">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a.</span><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">\u0414\u0438\u0441\u043a\u043e\u0432\u044b\u0439 \u0448\u0438\u0444\u0440\u0430\u0442\u043e\u0440</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0421\u043e\u0432\u043c\u0435\u0449\u0430\u0439\u0442\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u043d\u0430 \u0432\u0440\u0430\u0449\u0430\u044e\u0449\u0435\u043c\u0441\u044f \u0434\u0438\u0441\u043a\u0435 \u0441 \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u043c \u0442\u0435\u043a\u0441\u0442\u043e\u043c, \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u044f \u0442\u0430\u043a\u0438"
                        "\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435!<br /></span><span style=\" font-size:12pt; font-weight:700;\">\u041f\u0430\u043c\u044f\u0442\u043a\u0430:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043b\u044e\u0447, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u041a = \u042b. \u041a - \u0431\u0443\u043a\u0432\u0430 \u043d\u0430 \u0432\u043d\u0435\u0448\u043d\u0435\u043c \u0434\u0438\u0441\u043a\u0435, \u042b - \u0431\u0443\u043a\u0432\u0430 \u043d\u0430 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u043c \u0434\u0438\u0441\u043a\u0435.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span s"
                        "tyle=\" font-size:12pt;\">2) \u0421\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u0434\u0438\u0441\u043a \u0442\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u0447\u0442\u043e\u0431\u044b \u0431\u0443\u043a\u0432\u044b \u043a\u043b\u044e\u0447\u0430 \u043d\u0430\u0445\u043e\u0434\u0438\u043b\u0438\u0441\u044c \u0434\u0440\u0443\u0433 \u043d\u0430\u043f\u0440\u043e\u0442\u0438\u0432 \u0434\u0440\u0443\u0433\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3) \u041d\u0430\u0439\u0434\u0438\u0442\u0435 \u0431\u0443\u043a\u0432\u044b \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 \u043d\u0430 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u043c \u0434\u0438\u0441\u043a\u0435, \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0448\u0438\u0442\u0435 "
                        "\u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0431\u0443\u043a\u0432\u044b \u0432\u043d\u0435\u0448\u043d\u0435\u0433\u043e \u0434\u0438\u0441\u043a\u0430. \u0422\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u0435\u0441\u043b\u0438 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043b\u043e\u0432\u043e &quot;\u041f\u0440\u0438\u0432\u0435\u0442&quot; \u043f\u043e \u043a\u043b\u044e\u0447\u0443 \u041a = \u042b, \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0441\u044f &quot;\u042e\u044f\u0447\u0441\u0444\u0431&quot;.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4) \u0414\u043b\u044f \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438"
                        "\u0442\u043c: \u0441\u043e\u0432\u043c\u0435\u0449\u0430\u0439\u0442\u0435 \u0431\u0443\u043a\u0432\u044b \u0432\u043d\u0435\u0448\u043d\u0435\u0433\u043e \u0434\u0438\u0441\u043a\u0430 \u0441 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0433\u043e \u0434\u0438\u0441\u043a\u0430 \u0438 \u0437\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">\u0428\u0438\u0444\u0440 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u041e"
                        "\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442&quot;</span><span style=\" font-size:12pt;\"> - \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:12pt; font-weight:700;\">&quot;\u041a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f&quot;</span><span style=\" font-size:12pt;\"> - \u0441\u0442\u0440\u043e\u043a\u0430 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u043a\u043b\u044e\u0447\u0430 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f (\u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415: \u0435\u0441\u043b\u0438 \u043a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043d\u0435 \u0432\u0432\u0435\u0434\u0451\u043d, \u043f\u043e\u043b\u044f \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;/&quot"
                        ";\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0432\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0443\u0441\u0441\u043a\u0438"
                        "\u0439 \u0438 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\u0438.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u041f\u0440\u043e\u0447\u0438\u0435 \u0448\u0438\u0444\u0440\u0430\u0442\u043e\u0440\u044b</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;/&quot;\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0432\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:1"
                        "2pt; font-weight:700;\">&quot;\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span><span style=\" font-size:12pt;\"> - \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;Hash&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0438\u0442 \u0441\u0442\u0440\u043e\u043a\u0443 \u0432 \u0445\u044d\u0448. </span><span style=\" font-size:12pt; font-style:italic;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u043b\u044e\u0431\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;URL&quot;</span><span style=\" font-size:12pt;\"> - \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0438\u0442 \u0441\u0442\u0440\u043e\u043a\u0443 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442 URL-\u0441\u0442\u0440\u043e\u043a\u0438. </span><span style=\" font-size:12pt; font-style:italic;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">&quot;\u0410\u0442\u0431\u0430\u0448&quot;</span><span style=\" font-size:12pt;\"> - \u0448\u0438\u0444\u0440\u0443\u0435\u0442 \u0441\u0442\u0440\u043e\u043a\u0443 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0448\u0438\u0444\u0440\u0430 \u0410\u0442\u0431\u0430\u0448. </span"
                        "><span style=\" font-size:12pt; font-style:italic;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u00a9 \u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0438\u043d \u041f\u043e\u0434\u0443\u0448\u043a\u043e. \u0412\u0441\u0435 \u043f\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u044b. \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439 \u0448\u0438\u0444\u0440\u0430\u0442\u043e\u0440.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_program), QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

