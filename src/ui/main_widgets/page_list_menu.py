from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_widgets.menu_item import MenuItem


class PageListMenu(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.__initUI()
        self.__settingUI()
        
    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QVBoxLayout()
        self.product_item = MenuItem(self)
        self.users_item = MenuItem(self)
        self.orders_item = MenuItem(self)

    def __settingUI(self) -> None:
        self.setMaximumWidth(150)
        self.setLayout(self.main_h_layout)

        self.main_h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.main_h_layout.setContentsMargins(5, 5, 5, 5)

        self.opened_widget = self.product_item

        self.product_item.setup(icon_name='product.png', title="Products")
        self.users_item.setup(icon_name='users.png', title="Users")
        self.orders_item.setup(icon_name='orders.png', title='Orders')

        self.main_h_layout.addWidget(self.product_item)
        self.main_h_layout.addWidget(self.orders_item)
        self.main_h_layout.addWidget(self.users_item)

        self.product_item.setProperty("access_level", -1)
        self.orders_item.setProperty('access_level', 0)
        self.users_item.setProperty("access_level", 2)
