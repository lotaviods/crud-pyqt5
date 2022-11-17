from typing import Callable
from PyQt5 import QtCore, QtWidgets
from model.product import Product


class EditProductUiDialog(QtWidgets.QDialog):
    dialog: QtWidgets.QDialog
    callback: Callable[[Product], None]

    def __init__(self, product: Product, callback: Callable[[Product], None], parent=None):
        self.callback = callback
        self.product = product
        super(EditProductUiDialog, self).__init__(parent)

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Form")
        Dialog.resize(413, 229)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.id_label_hint = QtWidgets.QLabel(Dialog)
        self.id_label_hint.setMaximumSize(QtCore.QSize(30, 1000))
        self.id_label_hint.setObjectName("id_label_hint")
        self.horizontalLayout_4.addWidget(self.id_label_hint)
        self.id_label = QtWidgets.QLabel(Dialog)
        self.id_label.setText("")
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_4.addWidget(self.id_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_3.addWidget(self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout_3.addWidget(self.name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.price_label = QtWidgets.QLabel(Dialog)
        self.price_label.setObjectName("price_label")
        self.horizontalLayout_2.addWidget(self.price_label)
        self.price_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.price_lineEdit.setObjectName("price_lineEdit")
        self.horizontalLayout_2.addWidget(self.price_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stock_label = QtWidgets.QLabel(Dialog)
        self.stock_label.setObjectName("stock_label")
        self.horizontalLayout.addWidget(self.stock_label)
        self.stock_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.stock_lineEdit.setObjectName("stock_lineEdit")
        self.horizontalLayout.addWidget(self.stock_lineEdit)
        self.stock_pushButton_plus = QtWidgets.QPushButton(Dialog)
        self.stock_pushButton_plus.setObjectName("stock_pushButton_plus")
        self.horizontalLayout.addWidget(self.stock_pushButton_plus)
        self.stock_pushButton_minus = QtWidgets.QPushButton(Dialog)
        self.stock_pushButton_minus.setObjectName("stock_pushButton_minus")
        self.horizontalLayout.addWidget(self.stock_pushButton_minus)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.save_pushButton = QtWidgets.QPushButton(Dialog)
        self.save_pushButton.setObjectName("save_pushButton")
        self.verticalLayout.addWidget(self.save_pushButton)
        self.cancel_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.verticalLayout.addWidget(self.cancel_pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stock_pushButton_plus.clicked.connect(self.onStockPlusClick)
        self.stock_pushButton_minus.clicked.connect(self.onStockMinusClick)
        self.save_pushButton.clicked.connect(self.onSaveButtonClick)
        self.cancel_pushButton.clicked.connect(
            lambda: (
                self.dialog.close()
            )
        )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Editar produto"))
        self.id_label_hint.setText(_translate("Form", "id:"))
        self.name_label.setText(_translate("Form", "Nome"))
        self.price_label.setText(_translate("Form", "Preço"))
        self.stock_label.setText(_translate("Form", "Estoque"))
        self.stock_pushButton_plus.setText(_translate("Form", "+"))
        self.stock_pushButton_minus.setText(_translate("Form", " - "))
        self.save_pushButton.setText(_translate("Form", "Salvar"))
        self.cancel_pushButton.setText(_translate("Form", "Cancelar"))

        self.id_label.setText(str(self.product.id))
        self.name_lineEdit.setText(str(self.product.name))
        self.price_lineEdit.setText(str(self.product.price))
        self.stock_lineEdit.setText(str(self.product.stock))

    def onStockPlusClick(self):
        text = self.stock_lineEdit.text()
        number = -1
        try:
            number = int(text)
        except:
            pass
        self.product.stock = str(number + 1)

        self.stock_lineEdit.setText(self.product.stock)

    def onStockMinusClick(self):
        text = self.stock_lineEdit.text()
        number = -1
        try:
            number = int(text)
        except:
            pass
        self.product.stock = str(number - 1)

        self.stock_lineEdit.setText(self.product.stock)

    def makeProductByInput(self) -> Product:
        return Product(
            id=self.product.id,
            name=self.name_lineEdit.text(),
            price=self.price_lineEdit.text(),
            stock=self.stock_lineEdit.text()
        )

    def onSaveButtonClick(self):
        product = self.makeProductByInput()
        self.callback(product)
        self.dialog.accept()
