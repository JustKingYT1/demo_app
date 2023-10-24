from PySide6 import QtWidgets, QtCore, QtGui
from src.ui.api.resolvers import delete_product_in_order


class ProductInOrderItem(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.product_id = None
        self.order_id = None 
        self.title = QtWidgets.QLabel()
        self.count = QtWidgets.QLabel()
        self.cost = QtWidgets.QLabel()
        self.delete_button = QtWidgets.QPushButton()

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.main_h_layout.addWidget(self.title)
        self.main_h_layout.addWidget(self.cost)
        self.main_h_layout.addWidget(self.count)
        self.main_h_layout.addWidget(self.delete_button)

        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # self.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.title.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.count.setFrameShape(QtWidgets.QFrame.Shape.Box)

        # self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.title.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.cost.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.count.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.delete_button.setText('Delete')

        self.setFixedHeight(75)

        self.delete_button.clicked.connect(self.on_click_del_button)

    def set_product_info(self, productID: int, orderID: int, title: str, cost: int, count: int) -> None:
        self.product_id = productID
        self.order_id = orderID
        self.title.setText(str(title))
        self.cost.setText(str(cost))
        self.count.setText(str(count))

    def on_click_del_button(self) -> None:
        self.delete_product()

    def delete_product(self) -> None:
        delete_product_in_order(order_id=self.order_id, product_id=self.product_id)
        self.parent.update_products()
        self.parent.parent.product_list.update_products()