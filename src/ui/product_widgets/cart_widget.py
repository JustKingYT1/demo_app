from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_widgets.tools import get_pixmap_path, include_widgets
from ui.api.resolvers import get_all_products_in_order
from ui.orders_widgets.product_in_order_item import ProductInOrderItem
import threading
import random
from src.ui.api.resolvers import get_all_orders


class CartWidget(QtWidgets.QWidget):
    stop_flag = None
    add_product_signal: QtCore.Signal = QtCore.Signal(int, int, str, int, int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

        self.order_id = None
        
        self.statuslabel = ProductInOrderItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_h_layout.setContentsMargins(10, 10, 10, 0)
        self.main_v_layout.addLayout(self.tools_h_layout)
        self.main_v_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.statuslabel.delete_button.hide()
        
        self.scroll_layout.addWidget(self.statuslabel)
        
        self.statuslabel.set_product_info(0, 0, 'Title', 'Cost', 'Count')

        self.add_product_signal.connect(self.add_product_slot)
    
    def update_products(self) -> None:
        products = get_all_products_in_order(self.order_id if self.order_id else -1)['result']
        self.clear_products()
        if products:
            threading.Thread(target=self.load_products(products=products)).start()

    def load_products(self, products) -> None:
        for product in [products] if type(products) == dict else products:
            if self.stop_flag:
                exit()
                        
            self.add_product_signal.emit(
                product['productID'],
                product["orderID"],
                product["title"],
                product["cost"],
                product['count']
            )

    def set_order_id_in_cart_widget(self) -> int:
        order_id = random.randint(0, 255)
        for order in get_all_orders(self.parent.session.user.userID)["result"]:
            if order["ID"] == order_id:
                order_id = random.randint(0, 255)

        return order_id

    def add_product(self, product_id: int, order_id: int, title: str, cost: int, count: int) -> None:
        new_product = ProductInOrderItem(self)
        self.scroll_widget.__dict__.update({product_id: new_product})
        new_product.set_product_info(productID=int(product_id), orderID=int(order_id), title=str(title), cost=int(cost), count=int(count))
        self.scroll_layout.addWidget(new_product)
    
    def clear_products(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductInOrderItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    QtCore.Slot(int, int, str, int, int)
    def add_product_slot(self, product_id: int, order_id: int, title: str, cost: int, count: int) -> None:
        self.add_product(product_id=product_id, order_id=order_id, title=title, cost=cost, count=count)
        include_widgets(main_win=self.parent, elements=self.__dict__)