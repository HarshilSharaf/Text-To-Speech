# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Texttospeech(object):
    def setupUi(self, Texttospeech):
        Texttospeech.setObjectName("Texttospeech")
        Texttospeech.resize(578, 723)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Texttospeech.setWindowIcon(icon)
        Texttospeech.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Texttospeech)
        self.centralwidget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enterwordlab = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.enterwordlab.setFont(font)
        self.enterwordlab.setObjectName("enterwordlab")
        self.horizontalLayout.addWidget(self.enterwordlab)
        self.searchbox = QtWidgets.QLineEdit(self.frame_3)
        self.searchbox.setObjectName("searchbox")
        self.horizontalLayout.addWidget(self.searchbox)
        self.searchbutton = QtWidgets.QPushButton(self.frame_3)
        self.searchbutton.setObjectName("searchbutton")
        self.horizontalLayout.addWidget(self.searchbutton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.voicelab = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.voicelab.setFont(font)
        self.voicelab.setObjectName("voicelab")
        self.horizontalLayout_4.addWidget(self.voicelab)
        self.voicecombobox = QtWidgets.QComboBox(self.frame_3)
        self.voicecombobox.setStyleSheet("gridline-color: rgb(255, 255, 255);")
        self.voicecombobox.setObjectName("voicecombobox")
        self.horizontalLayout_4.addWidget(self.voicecombobox)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resultlab = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.resultlab.setFont(font)
        self.resultlab.setStyleSheet("background-color: rgb(33, 147, 176);")
        self.resultlab.setObjectName("resultlab")
        self.horizontalLayout_2.addWidget(self.resultlab)
        self.resultbox = QtWidgets.QTextEdit(self.frame_2)
        self.resultbox.setObjectName("resultbox")
        self.horizontalLayout_2.addWidget(self.resultbox)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.volumelab = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.volumelab.setFont(font)
        self.volumelab.setStyleSheet("border-color: rgb(255, 0, 0);")
        self.volumelab.setObjectName("volumelab")
        self.horizontalLayout_3.addWidget(self.volumelab)
        self.volumeslider = QtWidgets.QSlider(self.frame_2)
        self.volumeslider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeslider.setObjectName("volumeslider")
        self.horizontalLayout_3.addWidget(self.volumeslider)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        Texttospeech.setCentralWidget(self.centralwidget)

        self.retranslateUi(Texttospeech)
        QtCore.QMetaObject.connectSlotsByName(Texttospeech)

    def retranslateUi(self, Texttospeech):
        _translate = QtCore.QCoreApplication.translate
        Texttospeech.setWindowTitle(_translate("Texttospeech", "Text to Speech"))
        self.enterwordlab.setText(_translate("Texttospeech", "Enter Word:"))
        self.searchbox.setPlaceholderText(_translate("Texttospeech", "Type.."))
        self.searchbutton.setText(_translate("Texttospeech", "Search"))
        self.voicelab.setText(_translate("Texttospeech", "Voice:"))
        self.resultlab.setText(_translate("Texttospeech", "Result:"))
        self.volumelab.setText(_translate("Texttospeech", "Volume:"))
import temp_rc