from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
from src.ui.orders_widgets.product_in_order_item import ProductInOrderItem
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from src.ui.api.session import Session


class AddProductInCart(QtWidgets.QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()
    
    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        
        self.product = ProductInOrderItem(self)  

        self.confirm_button = QtWidgets.QPushButton()

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.product.count.hide()
        self.product.delete_button.hide()
        self.product.count_line_edit = QtWidgets.QLineEdit()
        self.product.main_h_layout.addWidget(self.product.count_line_edit)
        self.product.cost.setFixedSize(40, 40)
        self.product.title.setFixedSize(40, 40)
        self.product.cost.setText(self.product.cost.text() + ' p')
        self.confirm_button.setText('Add product')

        self.main_h_layout.addWidget(self.product, 3)
        self.main_h_layout.addWidget(self.confirm_button, 1)
        
        self.confirm_button.clicked.connect(self.on_click_confirm_button)

        self.setFixedHeight(80)

    def set_product_info(self, product_id, order_id, name, cost):
        self.product.set_product_info(productID=product_id, orderID=order_id, title=name, cost=cost, count=self.product.count_line_edit.text())
    
    def data_is_valid(self) -> bool:
        if not self.product.count_line_edit.text().isdigit():
            self.parent.parent.parent.show_message(text="Input integer value!", error=True, parent=self)
            return False
        
        return True
    
    def on_click_confirm_button(self) -> None:
        self.add()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return.numerator:
            self.add()

    def add(self) -> None:
        if not self.data_is_valid():
            return

        self.parent.buy_product(count=int(self.product.count_line_edit.text()))

        self.hide()
    

