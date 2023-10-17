from PySide6 import QtWidgets, QtCore, QtGui


class ProductItem(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.__initUI()
        self.__settingUI()
    
    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        
        self.product_id = QtWidgets.QLabel()
        self.name = QtWidgets.QLabel()
        self.cost = QtWidgets.QLabel()

        self.buy_button = QtWidgets.QPushButton()

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.main_h_layout.addWidget(self.product_id)
        self.main_h_layout.addWidget(self.name)
        self.main_h_layout.addWidget(self.cost)
        self.main_h_layout.addWidget(self.buy_button)

        self.buy_button.setText("Buy")
        self.buy_button.setProperty("access_level", 1)

        self.product_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.buy_button.setFixedWidth(40)


    def set_product_info(self, name: str, cost: int, productID: int) -> None:
        self.product_id.setText(str(productID))
        self.name.setText(name)
        self.cost.setText(str(cost))

        self.buy_button.clicked.connect(lambda: self.buy_product(productID=productID))

    def buy_product(self, productID: int) -> None:
        pass

    def product_updated(self) -> None:
        self.parent().update_products()