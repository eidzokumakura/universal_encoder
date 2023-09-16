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
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 651)
        MainWindow.setStyleSheet(u"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.caesar = QWidget()
        self.caesar.setObjectName(u"caesar")
        self.caesar.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font: 700 12pt \"Hack\";\n"
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
"QSlider::sub-page:horizontal {\n"
"    background-color: #090;\n"
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
"QLabel {\n"
"    font: 500 11pt \"Ubuntu\";\n"
"}\n"
"QSpinBox {\n"
"    border: 2px solid gra"
                        "y;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
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
        icon = QIcon()
        icon.addFile(u":/images/padlock_unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/padlock_locked.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/images/images/padlock_unlocked.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/images/images/padlock_locked.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.actio.setIcon(icon)
        self.actio.setCheckable(True)
        self.actio.setChecked(True)

        self.buttons.addWidget(self.actio)

        self.pushButton = QPushButton(self.caesar)
        self.pushButton.setObjectName(u"pushButton")

        self.buttons.addWidget(self.pushButton)


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
        self.about_program = QWidget()
        self.about_program.setObjectName(u"about_program")
        self.about_program.setStyleSheet(u"QLabel {\n"
"	text-align: center;\n"
"	margin: auto;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.about_program)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_about_program = QLabel(self.about_program)
        self.text_about_program.setObjectName(u"text_about_program")
        self.text_about_program.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.text_about_program)

        self.tabWidget.addTab(self.about_program, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.actio.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caesar), QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.wheel_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0435\u0441\u043e", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.inner_wheel.setText("")
        self.outer_wheel.setText("")
        self.key.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.disk), QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a\u043e\u0432\u044b\u0439", None))
        self.text_about_program.setText(QCoreApplication.translate("MainWindow", u"\u00a9 \u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0438\u043d \u041f\u043e\u0434\u0443\u0448\u043a\u043e \u0412\u0441\u0435 \u043f\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u044b. Universal Encoder.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_program), QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

