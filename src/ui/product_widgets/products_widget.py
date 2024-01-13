from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_widgets.tools import get_pixmap_path, include_widgets
from ui.api.resolvers import get_all_products, get_product, get_all_products_in_order
from ui.product_widgets.product_item import ProductItem
import threading
import time


class ProductsList(QtWidgets.QWidget):
    stop_flag = None
    add_product_signal: QtCore.Signal = QtCore.Signal(int, str, int)
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.last_keypress_time = 0
        self.keypress_interval = 0.2
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.product_search_line_edit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()
        
        self.statuslabel = ProductItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_h_layout.setContentsMargins(10, 10, 10, 0)
        self.main_v_layout.addLayout(self.tools_h_layout)
        self.main_v_layout.addWidget(self.scroll_area)
        self.tools_h_layout.addWidget(self.product_search_line_edit)
        self.tools_h_layout.addWidget(self.search_button)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.scroll_layout.addWidget(self.statuslabel)
        
        self.statuslabel.set_product_info('Name', 'Cost', 'ProductID')

        self.statuslabel.buy_button.setProperty('access_level', 10)

        self.search_button.setIcon(QtGui.QPixmap(get_pixmap_path("search.png")))
        self.search_button.setFixedSize(24, 24)
        self.search_button.setProperty("access_level", -1)
        self.product_search_line_edit.setProperty("access_level", -1)

        self.search_button.clicked.connect(self.on_find_button_click)
        self.add_product_signal.connect(self.add_product_slot)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        current_time = time.time()
        print(current_time)
        if event.key() == QtCore.Qt.Key.Key_Return.numerator and ((current_time - self.last_keypress_time) >= self.keypress_interval):
            self.last_keypress_time = current_time
            self.on_find_button_click()
    
    def on_find_button_click(self) -> None:
        products = get_product(self.product_search_line_edit.text())['result']
        self.update_products(products)
    
    def update_products(self, products=get_all_products()["result"]) -> None:
        self.clear_products()
        if products:
            threading.Thread(target=self.load_products, args=(products,)).start()

    def load_products(self, products) -> None:
        flag: bool = False
        for product in [products] if type(products) == dict else products:
            if self.stop_flag:
                exit()
                
            if self.parent.session.auth:
                products_in_order = get_all_products_in_order(self.parent.cart_widget.order_id)['result']
                if products_in_order:
                    for product_in_order in products_in_order:
                        if product_in_order['productID'] == product['ID']:
                            flag = True
                            break
                
                if flag:
                    flag = False
                    continue
                
            self.add_product_signal.emit(
                product["ID"],
                product["title"],
                product["cost"]
            )

    def add_product(self, product_id: int, name: str, cost: int) -> None:
        new_product = ProductItem(self)
        self.scroll_widget.__dict__.update({product_id: new_product})
        new_product.set_product_info(productID=int(product_id), name=str(name), cost=int(cost))
        self.scroll_layout.addWidget(new_product)
    
    def clear_products(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    QtCore.Slot(int, str, int)
    def add_product_slot(self, product_id: int, name: str, cost: int) -> None:
        self.add_product(product_id, name, cost)
        include_widgets(main_win=self.parent, elements=self.__dict__)