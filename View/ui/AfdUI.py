# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AFD.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 831)
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setObjectName("Main")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.Main)
        self.verticalLayout_45.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.tabWidget = QtWidgets.QTabWidget(self.Main)
        self.tabWidget.setObjectName("tabWidget")
        self.contrucaoTab = QtWidgets.QWidget()
        self.contrucaoTab.setObjectName("contrucaoTab")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.contrucaoTab)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.Form = QtWidgets.QFrame(self.contrucaoTab)
        self.Form.setAutoFillBackground(False)
        self.Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Form.setObjectName("Form")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.Form)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.qtd_input = QtWidgets.QGroupBox(self.Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.qtd_input.setFont(font)
        self.qtd_input.setObjectName("qtd_input")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.qtd_input)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.estados_l = QtWidgets.QFrame(self.qtd_input)
        self.estados_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.estados_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.estados_l.setObjectName("estados_l")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.estados_l)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.estados_l)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.qtd_estados = QtWidgets.QSpinBox(self.estados_l)
        self.qtd_estados.setObjectName("qtd_estados")
        self.verticalLayout_8.addWidget(self.qtd_estados)
        self.horizontalLayout_2.addWidget(self.estados_l)
        self.alfabeto_l = QtWidgets.QFrame(self.qtd_input)
        self.alfabeto_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alfabeto_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alfabeto_l.setObjectName("alfabeto_l")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.alfabeto_l)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.alfabeto_l)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.qtd_alfabeto = QtWidgets.QSpinBox(self.alfabeto_l)
        self.qtd_alfabeto.setObjectName("qtd_alfabeto")
        self.verticalLayout_3.addWidget(self.qtd_alfabeto)
        self.horizontalLayout_2.addWidget(self.alfabeto_l)
        self.qtd_funcoe_l = QtWidgets.QFrame(self.qtd_input)
        self.qtd_funcoe_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qtd_funcoe_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qtd_funcoe_l.setObjectName("qtd_funcoe_l")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.qtd_funcoe_l)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.qtd_funcoe_l)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.qtd_funcoes = QtWidgets.QSpinBox(self.qtd_funcoe_l)
        self.qtd_funcoes.setObjectName("qtd_funcoes")
        self.verticalLayout_9.addWidget(self.qtd_funcoes)
        self.horizontalLayout_2.addWidget(self.qtd_funcoe_l)
        self.estados_iniciais_l = QtWidgets.QFrame(self.qtd_input)
        self.estados_iniciais_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.estados_iniciais_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.estados_iniciais_l.setObjectName("estados_iniciais_l")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.estados_iniciais_l)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.estados_iniciais_l)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.qtd_estados_in = QtWidgets.QSpinBox(self.estados_iniciais_l)
        self.qtd_estados_in.setObjectName("qtd_estados_in")
        self.verticalLayout_12.addWidget(self.qtd_estados_in)
        self.horizontalLayout_2.addWidget(self.estados_iniciais_l)
        self.estados_finais_l = QtWidgets.QFrame(self.qtd_input)
        self.estados_finais_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.estados_finais_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.estados_finais_l.setObjectName("estados_finais_l")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.estados_finais_l)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.estados_finais_l)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.qtd_estados_fin = QtWidgets.QSpinBox(self.estados_finais_l)
        self.qtd_estados_fin.setObjectName("qtd_estados_fin")
        self.verticalLayout_2.addWidget(self.qtd_estados_fin)
        self.horizontalLayout_2.addWidget(self.estados_finais_l)
        self.verticalLayout_20.addWidget(self.qtd_input)
        self.info_input = QtWidgets.QGroupBox(self.Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.info_input.setFont(font)
        self.info_input.setObjectName("info_input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.info_input)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_15 = QtWidgets.QLabel(self.info_input)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.frame_13 = QtWidgets.QFrame(self.info_input)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_17.addWidget(self.label_14)
        self.estados = QtWidgets.QLineEdit(self.frame_13)
        self.estados.setObjectName("estados")
        self.verticalLayout_17.addWidget(self.estados)
        self.verticalLayout.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.info_input)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.alfabeto = QtWidgets.QLineEdit(self.frame_12)
        self.alfabeto.setObjectName("alfabeto")
        self.verticalLayout_16.addWidget(self.alfabeto)
        self.verticalLayout.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.info_input)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.info_input)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.estados_in = QtWidgets.QLineEdit(self.frame_10)
        self.estados_in.setObjectName("estados_in")
        self.verticalLayout_14.addWidget(self.estados_in)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.info_input)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.estados_fin = QtWidgets.QLineEdit(self.frame_9)
        self.estados_fin.setObjectName("estados_fin")
        self.verticalLayout_13.addWidget(self.estados_fin)
        self.verticalLayout.addWidget(self.frame_9)
        self.verticalLayout_20.addWidget(self.info_input)
        self.transicoes_input = QtWidgets.QGroupBox(self.Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.transicoes_input.setFont(font)
        self.transicoes_input.setObjectName("transicoes_input")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.transicoes_input)
        self.verticalLayout_18.setSpacing(7)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_14 = QtWidgets.QFrame(self.transicoes_input)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setWordWrap(False)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_19.addWidget(self.label_17)
        self.transicoes = QtWidgets.QPlainTextEdit(self.frame_14)
        self.transicoes.setObjectName("transicoes")
        self.verticalLayout_19.addWidget(self.transicoes)
        self.verticalLayout_18.addWidget(self.frame_14)
        self.verticalLayout_20.addWidget(self.transicoes_input)
        self.verticalLayout_43.addWidget(self.Form)
        self.tabWidget.addTab(self.contrucaoTab, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.tab_12)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.Form_2 = QtWidgets.QFrame(self.tab_12)
        self.Form_2.setAutoFillBackground(False)
        self.Form_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Form_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Form_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Form_2.setObjectName("Form_2")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.Form_2)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.info_input_2 = QtWidgets.QGroupBox(self.Form_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.info_input_2.setFont(font)
        self.info_input_2.setObjectName("info_input_2")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.info_input_2)
        self.verticalLayout_51.setSpacing(7)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_47 = QtWidgets.QLabel(self.info_input_2)
        self.label_47.setEnabled(True)
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setTextFormat(QtCore.Qt.AutoText)
        self.label_47.setWordWrap(False)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_51.addWidget(self.label_47)
        self.frame = QtWidgets.QFrame(self.info_input_2)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.entrada = QtWidgets.QLineEdit(self.frame)
        self.entrada.setObjectName("entrada")
        self.horizontalLayout.addWidget(self.entrada)
        self.testButton = QtWidgets.QPushButton(self.frame)
        self.testButton.setObjectName("testButton")
        self.horizontalLayout.addWidget(self.testButton)
        self.verticalLayout_51.addWidget(self.frame)
        self.label_37 = QtWidgets.QLabel(self.info_input_2)
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 14))
        self.label_37.setObjectName("label_37")
        self.verticalLayout_51.addWidget(self.label_37)
        self.resultado = QtWidgets.QLabel(self.info_input_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setText("")
        self.resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.resultado.setObjectName("resultado")
        self.verticalLayout_51.addWidget(self.resultado)
        spacerItem = QtWidgets.QSpacerItem(20, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_51.addItem(spacerItem)
        self.verticalLayout_44.addWidget(self.info_input_2)
        self.verticalLayout_59.addWidget(self.Form_2)
        self.tabWidget.addTab(self.tab_12, "")
        self.verticalLayout_45.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.Main)
    

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        
        """ 
        self.qtd_estados.setValue(3)
        self.qtd_alfabeto.setValue(2)
        self.qtd_funcoes.setValue(6)
        self.qtd_estados_in.setValue(1)
        self.qtd_estados_fin.setValue(1)
        self.estados.setText("S0 S1 S2")
        self.alfabeto.setText("0 1")
        self.estados_in.setText("S0")
        self.estados_fin.setText("S0")
        self.transicoes.setPlainText(""
        +"S0 S0 0 \n"
        +"S0 S1 1 \n"
        +"S1 S2 0 \n"
        +"S1 S0 1 \n"
        +"S2 S1 0 \n"
        +"S2 S2 1 \n")
        self.entrada.setText("0000000")
        """

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Construção</p><p><br/></p></body></html>"))
        self.qtd_input.setTitle(_translate("MainWindow", "Quantidades"))
        self.label_4.setText(_translate("MainWindow", "Estadados"))
        self.label_5.setText(_translate("MainWindow", "Alfabeto"))
        self.label_6.setText(_translate("MainWindow", "Funções"))
        self.label_9.setText(_translate("MainWindow", "Estadados Inciais"))
        self.label.setText(_translate("MainWindow", "Estadados Finais"))
        self.info_input.setTitle(_translate("MainWindow", "Informações"))
        self.label_15.setText(_translate("MainWindow", "Separe as informações por virgula!"))
        self.label_14.setText(_translate("MainWindow", "Digite os estados"))
        self.label_13.setText(_translate("MainWindow", "Digite o alfabeto"))
        self.label_11.setText(_translate("MainWindow", "Digite quais estados inciais"))
        self.label_10.setText(_translate("MainWindow", "Digite quais estados finais"))
        self.transicoes_input.setTitle(_translate("MainWindow", "Transições"))
        self.label_17.setText(_translate("MainWindow", "Digite as transições na seguinte ordem: <b>Estado atual - Estado de transicao - Caractere </b>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contrucaoTab), _translate("MainWindow", "Construção"))
        self.info_input_2.setTitle(_translate("MainWindow", "Teste"))
        self.label_47.setText(_translate("MainWindow", "Entrada"))
        self.testButton.setText(_translate("MainWindow", "Testar"))
        self.label_37.setText(_translate("MainWindow", "Resultado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Testes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())