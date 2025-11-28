# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fator_de_calibracaodrXDJb.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 717)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(32, 32, 32, 32)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_1 = QFrame(self.frame_2)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2.setTextFormat(Qt.TextFormat.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_6 = QFrame(self.frame_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.line_edit_fator = QLineEdit(self.frame_6)
        self.line_edit_fator.setObjectName(u"line_edit_fator")
        self.line_edit_fator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_fator.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.line_edit_fator)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame = QFrame(self.frame_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.btn_enviar = QPushButton(self.frame)
        self.btn_enviar.setObjectName(u"btn_enviar")

        self.horizontalLayout_2.addWidget(self.btn_enviar)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.frame_1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.group_dispositivo_serial = QGroupBox(self.frame_2)
        self.group_dispositivo_serial.setObjectName(u"group_dispositivo_serial")
        self.group_dispositivo_serial.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.verticalLayout_3 = QVBoxLayout(self.group_dispositivo_serial)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.group_dispositivo_serial)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.display_status = QLabel(self.frame_5)
        self.display_status.setObjectName(u"display_status")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.display_status.setFont(font2)

        self.horizontalLayout_4.addWidget(self.display_status)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cbox_seriais = QComboBox(self.group_dispositivo_serial)
        self.cbox_seriais.setObjectName(u"cbox_seriais")

        self.verticalLayout_3.addWidget(self.cbox_seriais)

        self.frame_4 = QFrame(self.group_dispositivo_serial)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_conectar = QPushButton(self.frame_4)
        self.btn_conectar.setObjectName(u"btn_conectar")

        self.horizontalLayout_3.addWidget(self.btn_conectar)

        self.btn_atualizar = QPushButton(self.frame_4)
        self.btn_atualizar.setObjectName(u"btn_atualizar")

        self.horizontalLayout_3.addWidget(self.btn_atualizar)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.group_dispositivo_serial)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_4)


        self.verticalLayout_4.addWidget(self.groupBox_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalSpacer = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_calcular = QPushButton(self.frame_7)
        self.btn_calcular.setObjectName(u"btn_calcular")

        self.horizontalLayout_6.addWidget(self.btn_calcular)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.line_edit_fator)
        self.label_3.setBuddy(self.lineEdit_4)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(self.line_edit_fator.selectAll)
        self.pushButton_3.clicked.connect(self.line_edit_fator.copy)
        self.pushButton_2.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fator de Calibra\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Resultado:", None))
        self.line_edit_fator.setText("")
        self.line_edit_fator.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vazio", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.group_dispositivo_serial.setTitle(QCoreApplication.translate("MainWindow", u"Dispositivo Serial: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Status de Conex\u00e3o:", None))
        self.display_status.setText(QCoreApplication.translate("MainWindow", u"Desconectado", None))
        self.btn_conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ajustes: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso Real: ", None))
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
    # retranslateUi

