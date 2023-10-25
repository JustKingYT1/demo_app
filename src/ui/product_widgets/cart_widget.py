from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_widgets.tools import get_pixmap_path, include_widgets
from ui.api.resolvers import get_all_products_in_order
from ui.orders_widgets.product_in_order_item import ProductInOrderItem
import threading
import random
from src.server.database.models import Orders, RemnantsOfProducts
from src.ui.api.resolvers import get_all_orders, create_order, get_all_warehouses_for_combo_box, get_remnants_of_products_in_warehouse, change_count_product_on_warehouse


class CartWidget(QtWidgets.QWidget):
    stop_flag = None
    add_product_signal: QtCore.Signal = QtCore.Signal(int, int, str, int, int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.sup_main_h_layout = QtWidgets.QHBoxLayout()
        self.tools_v_layout = QtWidgets.QVBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.warehouses_combo_box = QtWidgets.QComboBox()
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.create_button = QtWidgets.QPushButton()
        self.total_cost_layout = QtWidgets.QHBoxLayout()
        self.total_cost_label = QtWidgets.QLabel()
        self.total_cost_line_edit = QtWidgets.QLineEdit()

        self.order_id = None
        
        self.statuslabel = ProductInOrderItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.sup_main_h_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_v_layout.setContentsMargins(10, 10, 10, 0)
        self.main_h_layout.addLayout(self.sup_main_h_layout)
        self.sup_main_h_layout.addWidget(self.scroll_area, 10)
        self.sup_main_h_layout.addLayout(self.tools_v_layout, 1)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.total_cost_layout.addWidget(self.total_cost_label)
        self.total_cost_layout.addWidget(self.total_cost_line_edit)

        self.scroll_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.total_cost_line_edit.setEnabled(False)

        self.total_cost_label.setText('Total cost: ')

        self.total_cost_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.tools_v_layout.addLayout(self.total_cost_layout)
        self.tools_v_layout.addWidget(self.warehouses_combo_box)
        self.tools_v_layout.addWidget(self.create_button)

        self.create_button.setText('Confirm order!')

        self.statuslabel.delete_button.hide()
        
        self.fill_combo_box()

        self.scroll_layout.addWidget(self.statuslabel)
        
        self.statuslabel.set_product_info(0, 0, 'Title', 'Cost', 'Count')

        self.add_product_signal.connect(self.add_product_slot)
        self.create_button.clicked.connect(self.on_click_create_button)

    def calculate_total_cost(self) -> None:
        self.total_cost_line_edit.setText('0')
        products = get_all_products_in_order(self.order_id if self.order_id else -1)['result']
        if products:
            for product in products:
                self.total_cost_line_edit.setText(str(int(self.total_cost_line_edit.text()) + (product["cost"] * product["count"])))
    
    def update_products(self) -> None:
        products = get_all_products_in_order(self.order_id if self.order_id else -1)['result']
        self.clear_products()
        if products:
            threading.Thread(target=self.load_products(products=products)).start()
        
        self.calculate_total_cost()

    def load_products(self, products) -> None:
        for product in [products] if type(products) == dict else products:
            if self.stop_flag:
                exit()
                        
            self.add_product_signal.emit(
                product['productID'],
                product["orderID"],
                product["title"],
                product["count"],
                product['cost']
            )

    def on_click_create_button(self) -> None:
        self.create_order()

    def counter_products_on_warehouse(self) -> dict:
        products_in_order = get_all_products_in_order(self.order_id if self.order_id else -1)['result']
        products_on_warehouse = get_remnants_of_products_in_warehouse(int(self.warehouses_combo_box.currentText().replace(' ', '').split(':')[0]))['result']
        if not products_in_order:
            self.parent.show_message(text='Cart is empty', error=True, parent=self)
            return {'error': 'True'}
        list_products = []
        for product_on_warehouse in products_on_warehouse:
            for product_in_order in products_in_order:
                if product_in_order["productID"] == product_on_warehouse["productID"]:
                    if product_in_order["cost"] > product_on_warehouse["count"]:
                        list_products.append({'warehouse': product_on_warehouse, 'order': product_in_order})
        
        return {"error": False if len(list_products) == 0 else True, 'result': {'order': products_in_order, 'warehouse': products_on_warehouse} if len(list_products) == 0 else list_products}
    
    def change_products_on_warehouse(self) -> dict:
        res = self.counter_products_on_warehouse()
        if not res["error"]:
            for product_in_order, product_on_warehouse in zip(res['result']['order'], res['result']['warehouse']):
                change_count_product_on_warehouse(remnants=RemnantsOfProducts(
                    warehouseID=product_on_warehouse['warehouseID'],
                    productID=product_on_warehouse['productID'],
                    count=(product_on_warehouse['count'] - product_in_order['cost'])
                ))
            return res
        elif res['error'] == 'True':
            res['error'] =  True
            return res
        else:
            msg = f'Not enough on warehouse: '
            for product in res['result']:
                msg += f'productID: {product["warehouse"]["productID"]}, count: {product["warehouse"]["count"] - product["order"]["cost"]}, '
            
            self.parent.show_message(text=msg, error=True, parent=self)

            return res
            
    def create_order(self) -> None:
        products = self.change_products_on_warehouse()
        if products["error"]:
            return

        order = Orders(
            ID=self.order_id,
            accountID=self.parent.session.user.userID,
            track_number=str([random.randint(0, 15) for _ in range(0, 15)]).replace('[', '').replace(']', '').replace(',', '').replace(' ', ''),
            total_cost=int(self.total_cost_line_edit.text())
        )

        create_order(order=order)    

        self.order_id = self.set_order_id_in_cart_widget()

        self.update_products()

        self.parent.page_list.product_item.switch_page()

        self.parent.product_list.update_products()

        self.parent.orders_list.update_orders(get_all_orders(self.parent.session.user.userID)["result"])

        self.total_cost_line_edit.setText('')

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

    def fill_combo_box(self) -> None:
        for warehouse in get_all_warehouses_for_combo_box()["result"]:
            warehouse = f'{warehouse["ID"]}: {warehouse["name"]}'
            self.warehouses_combo_box.insertItem(self.warehouses_combo_box.count(), warehouse)

    def clear_products(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == ProductInOrderItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    QtCore.Slot(int, int, str, int, int)
    def add_product_slot(self, product_id: int, order_id: int, title: str, cost: int, count: int) -> None:
        self.add_product(product_id=product_id, order_id=order_id, title=title, cost=cost, count=count)
        include_widgets(main_win=self.parent, elements=self.__dict__)