# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_calc_with_file_btn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 301)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.field_layout = QtWidgets.QHBoxLayout()
        self.field_layout.setObjectName("field_layout")
        self.number_a_lbl = QtWidgets.QLabel(self.centralwidget)
        self.number_a_lbl.setObjectName("number_a_lbl")
        self.field_layout.addWidget(self.number_a_lbl)
        self.number_a_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_a_input.setObjectName("number_a_input")
        self.field_layout.addWidget(self.number_a_input)
        self.number_b_lbl = QtWidgets.QLabel(self.centralwidget)
        self.number_b_lbl.setObjectName("number_b_lbl")
        self.field_layout.addWidget(self.number_b_lbl)
        self.number_b_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_b_input.setObjectName("number_b_input")
        self.field_layout.addWidget(self.number_b_input)
        self.operation_lbl = QtWidgets.QLabel(self.centralwidget)
        self.operation_lbl.setObjectName("operation_lbl")
        self.field_layout.addWidget(self.operation_lbl)
        self.operation_input = QtWidgets.QLineEdit(self.centralwidget)
        self.operation_input.setObjectName("operation_input")
        self.field_layout.addWidget(self.operation_input)
        self.verticalLayout.addLayout(self.field_layout)
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setObjectName("btn_layout")
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.calculate_btn.setObjectName("calculate_btn")
        self.btn_layout.addWidget(self.calculate_btn)
        self.verticalLayout.addLayout(self.btn_layout)
        self.table_layout = QtWidgets.QHBoxLayout()
        self.table_layout.setObjectName("table_layout")
        self.result_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_table.sizePolicy().hasHeightForWidth())
        self.result_table.setSizePolicy(sizePolicy)
        self.result_table.setMinimumSize(QtCore.QSize(0, 0))
        self.result_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)
        self.table_layout.addWidget(self.result_table)
        self.verticalLayout.addLayout(self.table_layout)
        self.file_btn_layout = QtWidgets.QHBoxLayout()
        self.file_btn_layout.setObjectName("file_btn_layout")
        self.save_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_file_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.save_file_btn.setObjectName("save_file_btn")
        self.file_btn_layout.addWidget(self.save_file_btn)
        self.verticalLayout.addLayout(self.file_btn_layout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.number_a_lbl.setText(_translate("MainWindow", "Число А"))
        self.number_b_lbl.setText(_translate("MainWindow", "Число В"))
        self.operation_lbl.setText(_translate("MainWindow", "Операция"))
        self.calculate_btn.setText(_translate("MainWindow", "Вычислить значение"))
        self.save_file_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Сохранить данные выделенной строки таблицы в файл</p></body></html>"))
        self.save_file_btn.setText(_translate("MainWindow", "Сохранить данные в файл"))
