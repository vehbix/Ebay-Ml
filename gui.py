import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QButtonGroup
import socket


hc="a*/"

def send_message_to_server(message):
    # Sunucunun IP adresi ve port numarası
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 12345

    # Soket oluştur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Sunucuya bağlan
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Mesajı sunucuya gönder
    client_socket.send(message.encode())

    # Sunucudan gelen yanıtı al
    response = client_socket.recv(1024).decode()
    print("Sunucudan gelen yanıt:", response)

    # İstemci soketini kapat
    client_socket.close()
    return response

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_giris = QtWidgets.QPushButton(self.centralwidget)
        self.btn_giris.setGeometry(QtCore.QRect(170, 330, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_giris.setFont(font)
        self.btn_giris.setObjectName("btn_giris")
        self.label_giris = QtWidgets.QLabel(self.centralwidget)
        self.label_giris.setGeometry(QtCore.QRect(290, 330, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_giris.setFont(font)
        self.label_giris.setText("")
        self.label_giris.setObjectName("label_giris")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 200, 431, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtbx_mail = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtbx_mail.setFont(font)
        self.txtbx_mail.setObjectName("txtbx_mail")
        self.gridLayout.addWidget(self.txtbx_mail, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtbx_pass = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtbx_pass.setFont(font)
        self.txtbx_pass.setObjectName("txtbx_pass")
        self.gridLayout.addWidget(self.txtbx_pass, 1, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_giris.setText(_translate("MainWindow", "Giriş"))
        self.label.setText(_translate("MainWindow", "Mail"))
        self.label_2.setText(_translate("MainWindow", "Şifre"))

class Ui_AppWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 411, 441))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 391, 413))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lb_title = QtWidgets.QLineEdit(self.widget)
        self.lb_title.setObjectName("lb_title")
        self.gridLayout_3.addWidget(self.lb_title, 0, 1, 1, 1)


        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lb_category = QtWidgets.QLineEdit(self.widget)
        self.lb_category.setObjectName("lb_category")
        self.gridLayout_3.addWidget(self.lb_category, 1, 1, 1, 1)


        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.lb_shipcost = QtWidgets.QLineEdit(self.widget)
        self.lb_shipcost.setObjectName("lb_shipcost")
        self.gridLayout_3.addWidget(self.lb_shipcost, 2, 1, 1, 1)


        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.lb_shiptype = QtWidgets.QLineEdit(self.widget)
        self.lb_shiptype.setObjectName("lb_shiptype")
        self.gridLayout_3.addWidget(self.lb_shiptype, 3, 1, 1, 1)


        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.lb_shiploc = QtWidgets.QLineEdit(self.widget)
        self.lb_shiploc.setObjectName("lb_shiploc")
        self.gridLayout_3.addWidget(self.lb_shiploc, 4, 1, 1, 1)


        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.lb_onedayship = QtWidgets.QLineEdit(self.widget)
        self.lb_onedayship.setObjectName("lb_onedayship")
        self.gridLayout_3.addWidget(self.lb_onedayship, 5, 1, 1, 1)


        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.lb_handtime = QtWidgets.QLineEdit(self.widget)
        self.lb_handtime.setObjectName("lb_handtime")
        self.gridLayout_3.addWidget(self.lb_handtime, 6, 1, 1, 1) 


        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)          

        self.lb_bestoff = QtWidgets.QLineEdit(self.widget)
        self.lb_bestoff.setObjectName("lb_bestoff")
        self.gridLayout_3.addWidget(self.lb_bestoff, 7, 1, 1, 1)
        

        self.label_butitnow = QtWidgets.QLabel(self.widget)
        self.label_butitnow.setObjectName("label_butitnow")
        self.gridLayout_3.addWidget(self.label_butitnow, 8, 0, 1, 1)          

        self.lb_butitnow = QtWidgets.QLineEdit(self.widget)
        self.lb_butitnow.setObjectName("lb_butitnow")
        self.gridLayout_3.addWidget(self.lb_butitnow, 8, 1, 1, 1)


        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 9, 0, 1, 1)

        self.lb_gift = QtWidgets.QLineEdit(self.widget)
        self.lb_gift.setObjectName("lb_gift")
        self.gridLayout_3.addWidget(self.lb_gift, 9, 1, 1, 1)


        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 10, 0, 1, 1)

        self.lb_watchcount = QtWidgets.QLineEdit(self.widget)
        self.lb_watchcount.setObjectName("lb_watchcount")
        self.gridLayout_3.addWidget(self.lb_watchcount, 10, 1, 1, 1)


        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 11, 0, 1, 1)

        self.lb_returns = QtWidgets.QLineEdit(self.widget)
        self.lb_returns.setObjectName("lb_returns")
        self.gridLayout_3.addWidget(self.lb_returns, 11, 1, 1, 1)


        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 12, 0, 1, 1)

        self.lb_condit = QtWidgets.QLineEdit(self.widget)
        self.lb_condit.setObjectName("lb_condit")
        self.gridLayout_3.addWidget(self.lb_condit, 12, 1, 1, 1)
        

        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 13, 0, 1, 1)

        self.lb_toprated = QtWidgets.QLineEdit(self.widget)
        self.lb_toprated.setObjectName("lb_toprated")
        self.gridLayout_3.addWidget(self.lb_toprated, 13, 1, 1, 1)


        self.btn_gonder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gonder.setGeometry(QtCore.QRect(440, 480, 91, 41))
        self.btn_gonder.setObjectName("btn_gonder")

        self.gridLayout_3.setColumnMinimumWidth(0, 120)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 60, 125, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Title = QtWidgets.QRadioButton(self.splitter)
        self.Title.setObjectName("Title")


        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 50, 261, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        

        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)        
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        
        self.allData = QtWidgets.QRadioButton(self.splitter)
        self.allData.setObjectName("allData")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(440, 90, 256, 381))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setObjectName("listWidget")

        self.btnGetir = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetir.setGeometry(QtCore.QRect(440, 480, 91, 41))
        self.btnGetir.setObjectName("btnGetir")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(440, 90, 256, 381))
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setObjectName("listWidget_2")

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(440, 60, 164, 17))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        self.rdbtnTahmin = QtWidgets.QRadioButton(self.splitter_2)
        self.rdbtnTahmin.setChecked(True)
        self.rdbtnTahmin.setObjectName("rdbtnTahmin")

        self.rdbtnUrun = QtWidgets.QRadioButton(self.splitter_2)
        self.rdbtnUrun.setObjectName("rdbtnUrun")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuKaydet = QtWidgets.QMenu(self.menuFile)
        self.menuKaydet.setObjectName("menuKaydet")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDestek = QtWidgets.QMenu(self.menuHelp)
        self.menuDestek.setObjectName("menuDestek")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExel_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionExel_Kaydet.setObjectName("actionExel_Kaydet")
        self.actionCsv_kaydet = QtWidgets.QAction(MainWindow)
        self.actionCsv_kaydet.setObjectName("actionCsv_kaydet")
        self.actionYazd_r = QtWidgets.QAction(MainWindow)
        self.actionYazd_r.setObjectName("actionYazd_r")
        self.actionKullan_m_klavuzu = QtWidgets.QAction(MainWindow)
        self.actionKullan_m_klavuzu.setObjectName("actionKullan_m_klavuzu")
        self.actionMail_ileti_im = QtWidgets.QAction(MainWindow)
        self.actionMail_ileti_im.setObjectName("actionMail_ileti_im")
        self.actionEksik_r_n_bildirimi = QtWidgets.QAction(MainWindow)
        self.actionEksik_r_n_bildirimi.setObjectName("actionEksik_r_n_bildirimi")
        self.actionDestek_TAlebi = QtWidgets.QAction(MainWindow)
        self.actionDestek_TAlebi.setObjectName("actionDestek_TAlebi")
        self.action_leti_im = QtWidgets.QAction(MainWindow)
        self.action_leti_im.setObjectName("action_leti_im")
        self.actionTxt_Olarak_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionTxt_Olarak_Kaydet.setObjectName("actionTxt_Olarak_Kaydet")
        self.actionExel_Olarak_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionExel_Olarak_Kaydet.setObjectName("actionExel_Olarak_Kaydet")
        self.actionCsv_Olarak_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionCsv_Olarak_Kaydet.setObjectName("actionCsv_Olarak_Kaydet")
        self.menuKaydet.addAction(self.actionTxt_Olarak_Kaydet)
        self.menuKaydet.addAction(self.actionExel_Olarak_Kaydet)
        self.menuKaydet.addAction(self.actionCsv_Olarak_Kaydet)
        self.menuFile.addAction(self.menuKaydet.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionYazd_r)
        self.menuDestek.addAction(self.actionDestek_TAlebi)
        self.menuDestek.addAction(self.action_leti_im)
        self.menuHelp.addAction(self.actionKullan_m_klavuzu)
        self.menuHelp.addAction(self.menuDestek.menuAction())
        self.menuHelp.addAction(self.actionEksik_r_n_bildirimi)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

      

        self.Title.setChecked(True)
 
        self.lb_category.hide()
        self.lb_shipcost.hide()
        self.lb_shiptype.hide()
        self.lb_shiploc.hide()
        self.lb_onedayship.hide()
        self.lb_handtime.hide()
        self.lb_bestoff.hide()
        self.lb_butitnow.hide()
        self.lb_gift.hide()
        self.lb_watchcount.hide()
        self.lb_returns.hide()
        self.lb_condit.hide()
        self.lb_toprated.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_butitnow.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.listWidget_2.hide()
        self.btnGetir.hide()
        



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Ürün Bilgileri"))

        self.label.setText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "Category"))
        self.label_3.setText(_translate("MainWindow", "Shipping Cost"))
        self.label_4.setText(_translate("MainWindow", "Shipping Type"))
        self.label_5.setText(_translate("MainWindow", "Shipping Locations"))
        self.label_6.setText(_translate("MainWindow", "One Day Shipping"))
        self.label_7.setText(_translate("MainWindow", "Handling Time"))
        self.label_8.setText(_translate("MainWindow", "Best Offer"))
        self.label_butitnow.setText(_translate("MainWindow", "Buy It Now"))
        self.label_9.setText(_translate("MainWindow", "Gift"))
        self.label_10.setText(_translate("MainWindow", "Watch Count"))
        self.label_11.setText(_translate("MainWindow", "Returns"))
        self.label_12.setText(_translate("MainWindow", "Condition"))
        self.label_13.setText(_translate("MainWindow", "TopRated"))
        self.Title.setText(_translate("MainWindow", "Başlık"))
        self.allData.setText(_translate("MainWindow", "Tüm bilgiler"))
        self.btn_gonder.setText(_translate("MainWindow", "Gönder"))
        self.label_14.setText(_translate("MainWindow", "Fiyat Tahmini:"))
        self.btnGetir.setText(_translate("MainWindow", "Ürün Getir"))
        self.rdbtnTahmin.setText(_translate("MainWindow", "Analiz yap"))
        self.rdbtnUrun.setText(_translate("MainWindow", "Ürün Getir"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuKaydet.setTitle(_translate("MainWindow", "Kaydet"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDestek.setTitle(_translate("MainWindow", "Destek"))
        self.actionExel_Kaydet.setText(_translate("MainWindow", "Exel Kaydet"))
        self.actionCsv_kaydet.setText(_translate("MainWindow", "Csv kaydet"))
        self.actionYazd_r.setText(_translate("MainWindow", "Yazdır"))
        self.actionKullan_m_klavuzu.setText(_translate("MainWindow", "Kullanım klavuzu"))
        self.actionMail_ileti_im.setText(_translate("MainWindow", "İletişim"))
        self.actionEksik_r_n_bildirimi.setText(_translate("MainWindow", "Eksik ürün bildirimi"))
        self.actionDestek_TAlebi.setText(_translate("MainWindow", "Destek Talebi"))
        self.action_leti_im.setText(_translate("MainWindow", "İletişim"))
        self.actionTxt_Olarak_Kaydet.setText(_translate("MainWindow", "Txt Olarak Kaydet"))
        self.actionExel_Olarak_Kaydet.setText(_translate("MainWindow", "Exel Olarak Kaydet"))
        self.actionCsv_Olarak_Kaydet.setText(_translate("MainWindow", "Csv Olarak Kaydet"))

def loginCheck(ui,mail, password):
    # open_second_window_and_close_first(ui)
    # pass
    # if mail == "admin" and password == "admin":
    #     ui.label_giris.setText("Giriş başarılı 3 2 1 ...")
    #     QTimer.singleShot(3000, lambda:open_second_window_and_close_first(ui))
    #     return True
    # else:
    #     ui.label_giris.setText("Giriş başarısız")
    #     return False
    QTimer.singleShot(200, lambda:open_second_window_and_close_first(ui))
    return True

def check_radio_button(ui):
    
    if ui.allData.isChecked():
        ui.lb_category.show()
        ui.lb_shipcost.show()
        ui.lb_shiptype.show()
        ui.lb_shiploc.show()
        ui.lb_onedayship.show()
        ui.lb_handtime.show()
        ui.lb_bestoff.show()
        ui.lb_butitnow.show()
        ui.lb_gift.show()
        ui.lb_watchcount.show()
        ui.lb_returns.show()
        ui.lb_condit.show()
        ui.lb_toprated.show()
        ui.label_2.show()
        ui.label_3.show()
        ui.label_4.show()
        ui.label_5.show()
        ui.label_6.show()
        ui.label_7.show()
        ui.label_8.show()
        ui.label_butitnow.show()
        ui.label_9.show()
        ui.label_10.show()
        ui.label_11.show()
        ui.label_12.show()
        ui.label_13.show()
    if ui.Title.isChecked():
        ui.lb_category.hide()
        ui.lb_shipcost.hide()
        ui.lb_shiptype.hide()
        ui.lb_shiploc.hide()
        ui.lb_onedayship.hide()
        ui.lb_handtime.hide()
        ui.lb_bestoff.hide()
        ui.lb_butitnow.hide()
        ui.lb_gift.hide()
        ui.lb_watchcount.hide()
        ui.lb_returns.hide()
        ui.lb_condit.hide()
        ui.lb_toprated.hide()
        ui.label_2.hide()
        ui.label_3.hide()
        ui.label_4.hide()
        ui.label_5.hide()
        ui.label_6.hide()
        ui.label_7.hide()
        ui.label_8.hide()
        ui.label_butitnow.hide()
        ui.label_9.hide()
        ui.label_10.hide()
        ui.label_11.hide()
        ui.label_12.hide()
        ui.label_13.hide()

def check_radio_button_list(ui):
    if ui.rdbtnTahmin.isChecked():
        ui.listWidget.show()
        ui.btn_gonder.show()

        ui.listWidget_2.hide()
        ui.btnGetir.hide()

    if ui.rdbtnUrun.isChecked():
        ui.listWidget_2.show()
        ui.btnGetir.show()

        ui.listWidget.hide()
        ui.btn_gonder.hide()

def send_button_clicked(ui):
    
    if ui.Title.isChecked():
        title=ui.lb_title.text()
        message = title+hc
    if ui.allData.isChecked():
        title=ui.lb_title.text()
        category=ui.lb_category.text()
        shipcost=ui.lb_shipcost.text()
        shiptype=ui.lb_shiptype.text()
        shiploc=ui.lb_shiploc.text()
        onedayship=ui.lb_onedayship.text()
        handtime=ui.lb_handtime.text()
        bestoff=ui.lb_bestoff.text()
        buyitnow=ui.lb_butitnow.text()
        gift=ui.lb_gift.text()
        watchcount=ui.lb_watchcount.text()
        returns=ui.lb_returns.text()
        condit=ui.lb_condit.text()
        toprated=ui.lb_toprated.text()
        message = title + hc + category + hc + shipcost + hc + shiptype + hc + shiploc + hc + onedayship + hc + handtime + hc + bestoff + hc + buyitnow + hc+ gift + hc + watchcount + hc + returns + hc + condit + hc + toprated
    predict_price(ui, message)

def send_button_clicked_list(ui):
    if ui.rdbtnUrun.isChecked():
        title=ui.lb_title.text()
        message = title+hc+hc
        urun_getir(ui, message)


def add_data_to_list_widget(ui, data):
    # Clear the list widget before adding new data
    # ui.listWidget.clear()
    
    # # Add each item of the data list to the list widget
    # for item in data:
    #     ui.listWidget.addItem(item)
    ui.listWidget.addItem(data)

def add_data_to_list_urun_widget(ui, data):
    # Clear the list widget before adding new data
    # ui.listWidget.clear()
    
    # # Add each item of the data list to the list widget
    # for item in data:
    #     ui.listWidget.addItem(item)
    ui.listWidget_2.addItem(data)


def predict_price(ui, message):
    response = send_message_to_server(message)
    response=str(response)
    add_data_to_list_widget(ui, f"{response}$ {str(message.replace(hc, ' '))}")
    
    ui.label_15.setText(response)

def urun_getir(ui, message):
    response = send_message_to_server(message)
    response=str(response)
    add_data_to_list_urun_widget(ui, f"{response}")
    

def open_second_window_and_close_first(ui):
    global MainWindow, SecondWindow
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_AppWindow()
    ui.setupUi(SecondWindow)
    ui.Title.toggled.connect(lambda: check_radio_button(ui))
    ui.rdbtnTahmin.toggled.connect(lambda: check_radio_button_list(ui))
    ui.btn_gonder.clicked.connect(lambda: send_button_clicked(ui))
    ui.btnGetir.clicked.connect(lambda: send_button_clicked_list(ui))
    SecondWindow.show()
    MainWindow.close()

def login():
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow, SecondWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.btn_giris.clicked.connect(lambda: loginCheck(ui, ui.txtbx_mail.text(), ui.txtbx_pass.text()))
    

    sys.exit(app.exec_())


login()