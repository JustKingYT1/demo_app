from PySide6 import QtWidgets, QtCore, QtGui
from src.ui.main_widgets.tools import include_widgets
from src.ui.api.resolvers import get_all_orders, get_order
from src.ui.orders_widgets.product_in_order_item import ProductInOrderItem
import threading


class ProductListInOrder(QtWidgets.QDialog):
    stop_flag = None
    add_product_in_order_signal: QtCore.Signal = QtCore.Signal(str, int, int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

        self.statuslabel = ProductInOrderItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.main_v_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_layout.addWidget(self.statuslabel)
        self.statuslabel.set_product_info('Title', 'Cost', 'Count')

        self.add_product_in_order_signal.connect(self.add_order_slot)

    def update_list_in_order(self, products) -> None:
        if products:
            self.clear_products_in_order()
            threading.Thread(target=lambda: self.load_products_in_order(products)).start()

    def load_products_in_order(self, products) -> None:
        for order in [products] if type(products) == dict else products:
            if self.stop_flag:
                exit()

            self.add_product_in_order_signal.emit(
                order["title"],
                order["cost"],
                order["count"]
            )

    def add_product_in_order(self, title: str, cost: int, count: int) -> None:
        new_product = ProductInOrderItem(self)
        self.scroll_widget.__dict__.update({title: new_product})
        new_product.set_product_info(title=title, cost=cost, count=count)
        self.scroll_layout.addWidget(new_product)
        include_widgets(main_win=self.parent, elements=self.__dict__)

    def clear_products_in_order(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductInOrderItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    @QtCore.Slot(str, int, int)
    def add_order_slot(self, title: str, cost: int, count: int) -> None:
        self.add_product_in_order(title=title, cost=cost, count=count)
        include_widgets(main_win=self.parent, elements=self.__dict__)
