from PySide6 import QtWidgets, QtCore, QtGui
from src.ui.main_widgets.tools import get_pixmap_path


class ProductItem(QtWidgets.QFrame):
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

        self.buy_button.setFixedSize(24, 24)
        self.buy_button.setProperty("access_level", 0)
        self.buy_button.setIcon(QtGui.QPixmap(get_pixmap_path('buy.png')))

        self.product_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.buy_button.setFixedHeight(40)
        self.buy_button.setFixedWidth(40)

        # self.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.name.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.product_id.setFrameShape(QtWidgets.QFrame.Shape.Box)

        # self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.name.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.product_id.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.cost.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.setFixedHeight(80)

    def set_product_info(self, name: str, cost: int, productID: int) -> None:
        self.product_id.setText(str(productID))
        self.name.setText(name)
        self.cost.setText(str(cost))

        self.buy_button.clicked.connect(lambda: self.buy_product(productID=productID))

    def buy_product(self, productID: int) -> None:
        pass