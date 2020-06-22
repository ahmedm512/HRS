# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservation_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

#------------------IMPORTS----------------------------------------#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, Qt
import backend
import database_handling

#-----------------------Reservation Variables---------------------#
global room_no
global guest_name
global check_in
global check_out
global guest_id
global price
#-----------------------------------------------------------------#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 529)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(49, 19, 591, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.roomNo_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.roomNo_label.setObjectName("roomNo_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.roomNo_label)
        self.guistName_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.guistName_label.setObjectName("guistName_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.guistName_label)
        self.checkIn_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.checkIn_label.setObjectName("checkIn_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkIn_label)
        self.guistId_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.guistId_label.setObjectName("guistId_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.guistId_label)
        self.roomNo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.roomNo.setText("")
        self.roomNo.setPlaceholderText("")
        self.roomNo.setObjectName("roomNo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.roomNo)
        self.guestName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.guestName.setText("")
        self.guestName.setObjectName("guestName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.guestName)
        self.guestId = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.guestId.setObjectName("guestId")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.guestId)
        self.checkOut_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.checkOut_label.setObjectName("checkOut_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkOut_label)
        self.price_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.price_label.setObjectName("price_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.price_label)
        self.price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price.setInputMask("")
        self.price.setText("")
        self.price.setObjectName("price")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.price)
        self.checkIn = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.checkIn.setWrapping(False)
        self.checkIn.setReadOnly(False)
        self.checkIn.setSpecialValueText("")
        self.checkIn.setAccelerated(False)
        self.checkIn.setMinimumDate(QDate.currentDate())
        self.checkIn.setCalendarPopup(True)
        self.checkIn.setObjectName("checkIn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkIn)
        self.checkOut = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.checkOut.setDisplayFormat("dd/MM/yyyy")
        self.checkOut.setMinimumDate(QDate.currentDate().addDays(+1))
        self.checkOut.setCalendarPopup(True)
        self.checkOut.setObjectName("checkOut")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkOut)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 370, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.makeReservation = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.makeReservation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.makeReservation.setObjectName("makeReservation")
        self.horizontalLayout.addWidget(self.makeReservation)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCAlender = QtWidgets.QAction(MainWindow)
        self.actionCAlender.setObjectName("actionCAlender")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionCAlender)
        self.menubar.addAction(self.menuFile.menuAction())

    #-----------------Connections-------------------------#
        self.makeReservation.clicked.connect(self.reservationClicked)
        self.cancel.clicked.connect(self.cancelClicked)

    #-----------------------------------------------------#

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.roomNo_label.setText(_translate("MainWindow", "Room No."))
        self.guistName_label.setText(_translate("MainWindow", "Guist Name"))
        self.checkIn_label.setText(_translate("MainWindow", "Check In"))
        self.guistId_label.setText(_translate("MainWindow", "Guist ID"))
        self.checkOut_label.setText(_translate("MainWindow", "Check Out"))
        self.price_label.setText(_translate("MainWindow", "Price"))
        self.checkIn.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.makeReservation.setText(_translate("MainWindow", "Make Reservation"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Make Reservation"))
        self.actionCAlender.setText(_translate("MainWindow", "Reserved Table"))


    def reservationClicked(self):
        try:
            room_no = int(self.roomNo.text())
            #self.roomNo.setText("")
            if not(0 < room_no < 30):
                self.show_popup('Room Number Does not exist', 'w')
            print(room_no)

            guest_name = self.guestName.text()
            if not(guest_name):
                self.show_popup('Please Enter Guest Name', 'w')
            #self.guestName.setText("")
            print(guest_name)

            check_in = self.checkIn.date().toPyDate()
            print(check_in)

            check_out = self.checkOut.date().toPyDate()
            print(check_out)

            guest_id = int(self.guestId.text())
            print(guest_id)
            if not (guest_id):
                self.show_popup('Please Enter Guest ID', 'w')

            price = int(self.price.text())
            print(price)
            if not (price):
                self.show_popup('Please Enter Price', 'w')

            if backend.checkin(room_no, guest_name, check_in, price, guest_id, check_out):
                # History table to be added
                self.show_popup(f'Room {room_no} is Reserved', 'i')
            else:
                self.show_popup('Room is already reserved OR something went wrong', 'c')
        except:
            self.show_popup('Please Enter a Valid Input', 'w')



    def cancelClicked(self):
        self.roomNo.setText("")
        self.guestName.setText("")
        self.price.setText("")
        self.guestId.setText("")

    def show_popup(self, error_message, icon):
        msg = QMessageBox()
        msg.setWindowTitle("Message Box")
        msg.setText(error_message)
        if icon == 'i':
            msg.setIcon(QMessageBox.Information)
        elif icon == 'w':
            msg.setIcon(QMessageBox.Warning)
        elif icon == 'c':
            msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
