# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\MyProjects\GUI_project\wo_upload.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wo_upload(object):
    def setupUi(self, wo_upload):
        wo_upload.setObjectName("wo_upload")
        wo_upload.resize(1024, 600)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        wo_upload.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/resources/linux_216px_1210908_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wo_upload.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(wo_upload)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bt_upload = QtWidgets.QPushButton(self.centralwidget)
        self.bt_upload.setObjectName("bt_upload")
        self.horizontalLayout_2.addWidget(self.bt_upload)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.bt_update = QtWidgets.QPushButton(self.centralwidget)
        self.bt_update.setObjectName("bt_update")
        self.horizontalLayout_2.addWidget(self.bt_update)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_wo = QtWidgets.QLabel(self.centralwidget)
        self.lb_wo.setObjectName("lb_wo")
        self.verticalLayout.addWidget(self.lb_wo)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.lb_aproval_no = QtWidgets.QLabel(self.centralwidget)
        self.lb_aproval_no.setObjectName("lb_aproval_no")
        self.verticalLayout.addWidget(self.lb_aproval_no)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.lb_prod = QtWidgets.QLabel(self.centralwidget)
        self.lb_prod.setObjectName("lb_prod")
        self.verticalLayout.addWidget(self.lb_prod)
        spacerItem9 = QtWidgets.QSpacerItem(82, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.lb_prod_qty = QtWidgets.QLabel(self.centralwidget)
        self.lb_prod_qty.setObjectName("lb_prod_qty")
        self.verticalLayout.addWidget(self.lb_prod_qty)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.lb_date_toWH = QtWidgets.QLabel(self.centralwidget)
        self.lb_date_toWH.setObjectName("lb_date_toWH")
        self.verticalLayout.addWidget(self.lb_date_toWH)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_wo = QtWidgets.QLineEdit(self.centralwidget)
        self.le_wo.setObjectName("le_wo")
        self.verticalLayout_2.addWidget(self.le_wo)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.le_approval_no = QtWidgets.QLineEdit(self.centralwidget)
        self.le_approval_no.setObjectName("le_approval_no")
        self.verticalLayout_2.addWidget(self.le_approval_no)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        spacerItem13 = QtWidgets.QSpacerItem(185, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.le_prod_qty = QtWidgets.QLineEdit(self.centralwidget)
        self.le_prod_qty.setObjectName("le_prod_qty")
        self.verticalLayout_2.addWidget(self.le_prod_qty)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.dateEdit_date_toWH = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_date_toWH.setObjectName("dateEdit_date_toWH")
        self.verticalLayout_2.addWidget(self.dateEdit_date_toWH)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem15 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lb_guy_send = QtWidgets.QLabel(self.centralwidget)
        self.lb_guy_send.setObjectName("lb_guy_send")
        self.verticalLayout_3.addWidget(self.lb_guy_send)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.lb_guy_receive = QtWidgets.QLabel(self.centralwidget)
        self.lb_guy_receive.setObjectName("lb_guy_receive")
        self.verticalLayout_3.addWidget(self.lb_guy_receive)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem17)
        self.lb_current_node = QtWidgets.QLabel(self.centralwidget)
        self.lb_current_node.setObjectName("lb_current_node")
        self.verticalLayout_3.addWidget(self.lb_current_node)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem18)
        self.label_chip = QtWidgets.QLabel(self.centralwidget)
        self.label_chip.setObjectName("label_chip")
        self.verticalLayout_3.addWidget(self.label_chip)
        spacerItem19 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem19)
        self.lb_remarks = QtWidgets.QLabel(self.centralwidget)
        self.lb_remarks.setObjectName("lb_remarks")
        self.verticalLayout_3.addWidget(self.lb_remarks)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.le_guy_send = QtWidgets.QLineEdit(self.centralwidget)
        self.le_guy_send.setPlaceholderText("")
        self.le_guy_send.setObjectName("le_guy_send")
        self.verticalLayout_4.addWidget(self.le_guy_send)
        spacerItem20 = QtWidgets.QSpacerItem(145, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem20)
        self.le_guy_receive = QtWidgets.QLineEdit(self.centralwidget)
        self.le_guy_receive.setPlaceholderText("")
        self.le_guy_receive.setObjectName("le_guy_receive")
        self.verticalLayout_4.addWidget(self.le_guy_receive)
        spacerItem21 = QtWidgets.QSpacerItem(145, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem21)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        spacerItem22 = QtWidgets.QSpacerItem(145, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem22)
        self.comboBox_chip = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_chip.setObjectName("comboBox_chip")
        self.comboBox_chip.addItem("")
        self.comboBox_chip.addItem("")
        self.comboBox_chip.addItem("")
        self.comboBox_chip.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_chip)
        spacerItem23 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem23)
        self.le_remarks = QtWidgets.QLineEdit(self.centralwidget)
        self.le_remarks.setObjectName("le_remarks")
        self.verticalLayout_4.addWidget(self.le_remarks)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem24)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        wo_upload.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wo_upload)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        wo_upload.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wo_upload)
        self.statusbar.setObjectName("statusbar")
        wo_upload.setStatusBar(self.statusbar)

        self.retranslateUi(wo_upload)
        QtCore.QMetaObject.connectSlotsByName(wo_upload)

    def retranslateUi(self, wo_upload):
        _translate = QtCore.QCoreApplication.translate
        wo_upload.setWindowTitle(_translate("wo_upload", "派工单上传"))
        self.bt_upload.setText(_translate("wo_upload", "上传数据库"))
        self.bt_update.setText(_translate("wo_upload", "更新数据库"))
        self.lb_wo.setText(_translate("wo_upload", "派工单号："))
        self.lb_aproval_no.setText(_translate("wo_upload", "审批编号："))
        self.lb_prod.setText(_translate("wo_upload", "产品形态："))
        self.lb_prod_qty.setText(_translate("wo_upload", "生产数量："))
        self.lb_date_toWH.setText(_translate("wo_upload", "入库日期："))
        self.le_wo.setText(_translate("wo_upload", "X201911"))
        self.le_approval_no.setPlaceholderText(_translate("wo_upload", "填写审批编号后6位"))
        self.comboBox.setItemText(0, _translate("wo_upload", "单相表"))
        self.comboBox.setItemText(1, _translate("wo_upload", "13版三相表"))
        self.comboBox.setItemText(2, _translate("wo_upload", "13版集中器"))
        self.comboBox.setItemText(3, _translate("wo_upload", "I型采集器"))
        self.comboBox.setItemText(4, _translate("wo_upload", "II型采集器"))
        self.comboBox.setItemText(5, _translate("wo_upload", "抄控器"))
        self.comboBox.setItemText(6, _translate("wo_upload", "09版三相表"))
        self.comboBox.setItemText(7, _translate("wo_upload", "09版集中器"))
        self.comboBox.setItemText(8, _translate("wo_upload", "充电网关"))
        self.comboBox.setItemText(9, _translate("wo_upload", "充电插座"))
        self.comboBox.setItemText(10, _translate("wo_upload", "集中器微功率模块"))
        self.comboBox.setItemText(11, _translate("wo_upload", "三相耦合器"))
        self.le_prod_qty.setPlaceholderText(_translate("wo_upload", "必须填写整数"))
        self.lb_guy_send.setText(_translate("wo_upload", "入库人号："))
        self.lb_guy_receive.setText(_translate("wo_upload", "接收人员："))
        self.lb_current_node.setText(_translate("wo_upload", "当前节点："))
        self.label_chip.setText(_translate("wo_upload", "芯片方案："))
        self.lb_remarks.setText(_translate("wo_upload", "补充说明："))
        self.le_guy_send.setText(_translate("wo_upload", "谢丽花"))
        self.le_guy_receive.setText(_translate("wo_upload", "柳元权"))
        self.comboBox_2.setItemText(0, _translate("wo_upload", "备料"))
        self.comboBox_2.setItemText(1, _translate("wo_upload", "改造"))
        self.comboBox_2.setItemText(2, _translate("wo_upload", "升级"))
        self.comboBox_2.setItemText(3, _translate("wo_upload", "刻印"))
        self.comboBox_2.setItemText(4, _translate("wo_upload", "测试"))
        self.comboBox_2.setItemText(5, _translate("wo_upload", "包装"))
        self.comboBox_2.setItemText(6, _translate("wo_upload", "报检"))
        self.comboBox_2.setItemText(7, _translate("wo_upload", "入库"))
        self.comboBox_2.setItemText(8, _translate("wo_upload", "返工"))
        self.comboBox_chip.setItemText(0, _translate("wo_upload", "3105"))
        self.comboBox_chip.setItemText(1, _translate("wo_upload", "3911"))
        self.comboBox_chip.setItemText(2, _translate("wo_upload", "STKS_CCV1.30"))
        self.comboBox_chip.setItemText(3, _translate("wo_upload", "STKS_CCV1.31"))
        self.le_remarks.setPlaceholderText(_translate("wo_upload", "根据实际情况选填"))
import apprcc_rc
