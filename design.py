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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QTextEdit {\n"
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
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.original_text = QVBoxLayout()
        self.original_text.setObjectName(u"original_text")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.original_text.addWidget(self.label)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.original_text.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.original_text)

        self.encrypted_decrypted_text = QVBoxLayout()
        self.encrypted_decrypted_text.setObjectName(u"encrypted_decrypted_text")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.encrypted_decrypted_text.addWidget(self.label_2)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.encrypted_decrypted_text.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.encrypted_decrypted_text)

        self.buttons = QHBoxLayout()
        self.buttons.setObjectName(u"buttons")
        self.encrypt = QPushButton(self.centralwidget)
        self.encrypt.setObjectName(u"encrypt")
        icon = QIcon()
        icon.addFile(u":/images/padlock_unlocked.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/padlock_locked.svg", QSize(), QIcon.Normal, QIcon.On)
        self.encrypt.setIcon(icon)
        self.encrypt.setCheckable(True)
        self.encrypt.setChecked(True)

        self.buttons.addWidget(self.encrypt)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.buttons.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.buttons.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.buttons)

        self.slider = QHBoxLayout()
        self.slider.setObjectName(u"slider")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.slider.addWidget(self.label_3)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.slider.addWidget(self.horizontalSlider)

        self.spinBox = QSpinBox(self.centralwidget)
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

        self.label_4 = QHBoxLayout()
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addLayout(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 / \u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.encrypt.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Actio!", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u0430\u0442\u043e\u0440\u044b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

