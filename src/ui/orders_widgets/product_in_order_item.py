from PySide6 import QtWidgets, QtCore, QtGui


class ProductInOrderItem(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()

        self.title = QtWidgets.QLabel()
        self.count = QtWidgets.QLabel()
        self.cost = QtWidgets.QLabel()

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.main_h_layout.addWidget(self.title)
        self.main_h_layout.addWidget(self.cost)
        self.main_h_layout.addWidget(self.count)

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

        self.setFixedHeight(75)

    def set_product_info(self, title: str, cost: int, count: int) -> None:
        self.title.setText(str(title))
        self.cost.setText(str(cost))
        self.count.setText(str(count))

