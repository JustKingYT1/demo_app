from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtGui
from src.ui.main_widgets.tools import include_widgets
from src.ui.api.resolvers import get_all_orders, get_order
from src.ui.orders_widgets.product_in_order_item import ProductInOrderItem
import threading


class ProductListInOrder(QtWidgets.QDialog):
    stop_flag = None
    add_product_in_order_signal: QtCore.Signal = QtCore.Signal(int, int, str, int, int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QHBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

        self.total_cost_label = QtWidgets.QLabel()
        self.total_cost_line_edit = QtWidgets.QLineEdit()
        self.total_cost_layout = QtWidgets.QVBoxLayout()

        self.statuslabel = ProductInOrderItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_v_layout)
        self.resize(300, 400)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.main_v_layout.addWidget(self.scroll_area, 10)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.total_cost_label.setText('Total cost: ')
        self.total_cost_line_edit.setEnabled(False)
        self.total_cost_layout.addWidget(self.total_cost_label)
        self.total_cost_layout.addWidget(self.total_cost_line_edit)
        self.total_cost_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.main_v_layout.addLayout(self.total_cost_layout, 1)
        self.scroll_layout.addWidget(self.statuslabel)
        self.statuslabel.delete_button.hide()
        self.statuslabel.set_product_info(0, 0, 'Title', 'Cost', 'Count')

        self.scroll_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.add_product_in_order_signal.connect(self.add_product_in_order_slot)

    def set_total_cost_in_order_list(self, total_cost: int) -> None:
        self.total_cost_line_edit.setText(str(total_cost))

    def update_products_in_order(self, products) -> None:
        self.clear_products_in_order()
        if products:
            threading.Thread(target=lambda: self.load_products_in_order(products)).start()

    def load_products_in_order(self, products) -> None:
        for product in [products] if type(products) == dict else products:
            if self.stop_flag:
                exit()

            self.add_product_in_order_signal.emit(
                product["productID"],
                product["orderID"],
                product["title"],
                product["cost"],
                product["count"]
            )

    def add_product_in_order(self, product_id: int, order_id: int, title: str, cost: int, count: int) -> None:
        new_product = ProductInOrderItem(self)
        new_product.delete_button.hide()
        self.scroll_widget.__dict__.update({product_id: new_product})
        new_product.set_product_info(productID=product_id, orderID=order_id, title=title, cost=cost, count=count)
        self.scroll_layout.addWidget(new_product)

    def clear_products_in_order(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductInOrderItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    @QtCore.Slot(int, int, str, int, int)
    def add_product_in_order_slot(self, product_id: int, order_id: int, title: str, cost: int, count: int) -> None:
        self.add_product_in_order(product_id=product_id, order_id=order_id, title=title, cost=cost, count=count)

    def closeEvent(self, arg__1: QtGui.QCloseEvent) -> None:
        self.destroy()