from PySide6 import QtWidgets, QtCore, QtGui
from ui.tools import get_pixmap_path
from ui.api.resolvers import get_all_products, get_product
from ui.tools import include_widgets
from server.database.models import Products
from ui.product_item import ProductItem
import threading

class ProductsList(QtWidgets.QWidget):
    stop_flag = None
    add_product_signal: QtCore.Signal = QtCore.Signal(int, str, int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.product_search_line_edit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

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

        self.search_button.setIcon(QtGui.QPixmap(get_pixmap_path("search.png")))
        self.search_button.setFixedSize(24, 24)
        self.search_button.setProperty("access_level", -1)
        self.product_search_line_edit.setProperty("access_level", -1)

        self.search_button.clicked.connect(self.on_find_button_click)
        self.add_product_signal.connect(self.add_product)

    def validate_data(self) -> bool:
        return True if self.product_search_line_edit.text().isdigit() else False
    
    def on_find_button_click(self) -> None:
        # if not self.validate_data():
        #     self.parent.show_message(text="Search field must contains integer value", error=True, parent=self)
        #     return
        
        products = get_product(self.product_search_line_edit.text())["result"]

        self.update_products(products)
        
    
    def update_products(self, products=get_all_products()["result"]) -> None:
        self.clear_products()
        threading.Thread(target=lambda: self.load_products(products)).start()

    def load_products(self, products) -> None:
        print(type(products))
        products = (products,)
        for product in [products[0]] if type(products[0]) == dict else products[0]:
            if self.stop_flag:
                exit()
            
            print(product, type(products[0]) == dict)
            
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
        include_widgets(main_win=self.parent, elements=self.__dict__)
    
    def clear_products(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    QtCore.Slot(int, str, int)
    def add_procuct_slot(self, product_id: int, name: str, cost: int) -> None:
        self.add_product(product_id, name, cost)
        include_widgets(parent=self.parent(), elements=self.__dict__)