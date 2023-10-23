from PySide6 import QtCore, QtWidgets, QtGui
from ui.api import resolvers
from src.ui.api.session import Session
from ui.dialog_forms.sign_in_form import SignWindow
from ui.orders_widgets.orders_list import OrdersList
from ui.main_widgets.page_list_menu import PageListMenu
from ui.product_widgets.products_list import ProductsList
from ui.main_widgets.tools import include_widgets
from ui.main_widgets.authorization_menu import AuthorizationMenu
from ui.main_widgets.user_profile import UserProfile
import multiprocessing
from ui.api.resolvers import get_all_orders
import sys
from src.ui.product_widgets.cart_widget import CartWidget
import json

sys.path.append('C:/demo_app/src')

from start_server import start_server

class MainWindow(QtWidgets.QMainWindow):
    session: Session = Session()

    def __init__(self) -> None:
        super().__init__()
        self.start_server()
        if self.__connect_check():
            if self.__connect_check()["code"] == 400:
                self.show_message(text=self.__connect_check()["msg"], error=True, parent=self)
                self.server_process.terminate()
                exit()
        
        sign_window = SignWindow(self)
        sign_window.show()
        sign_window.exec_()

        if self.session.user.userID == -1:
            self.server_process.terminate()
            exit()

        self.__initUI()
        self.__settingUI()
        self.show()
    
    @staticmethod
    @resolvers.server_available
    def __connect_check() -> None:
        return {"code": 200, 'msg': 'Succesfully', 'error': False, 'result': None}

    def __initUI(self) -> None:
        self.central_widget = QtWidgets.QWidget(self)
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.widget_container = QtWidgets.QWidget(self)
        self.widget_container_layout = QtWidgets.QVBoxLayout()
        self.page_list = PageListMenu(self)
        self.product_list = ProductsList(self)
        self.orders_list = OrdersList(self)
        self.cart_widget = CartWidget(self)
        self.user_profile = UserProfile(self)
        self.authorization_menu = AuthorizationMenu(self)

    def __settingUI(self) -> None:
        self.resize(930, 615)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)
        self.widget_container.setLayout(self.widget_container_layout)
        self.main_h_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_container_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_container_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.main_h_layout.addWidget(self.page_list)
        self.main_h_layout.addWidget(self.widget_container)
        self.main_h_layout.addWidget(self.authorization_menu)
        self.main_h_layout.addWidget(self.user_profile)

        self.widget_container_layout.addWidget(self.cart_widget)
        self.widget_container_layout.addWidget(self.product_list)
        self.widget_container_layout.addWidget(self.orders_list)
        self.page_list.product_item.bind_widget(self.product_list)
        self.page_list.users_item.bind_widget(self.product_list)
        self.page_list.orders_item.bind_widget(self.orders_list)
        self.page_list.cart_item.bind_widget(self.cart_widget)

        self.get_order_id_in_offline_app()

        self.product_list.update_products()
        self.orders_list.update_orders(get_all_orders(self.session.user.userID)["result"])
        self.cart_widget.update_products()

        include_widgets(main_win=self, elements=self.__dict__)

        self.user_profile.hide()

        self.page_list.product_item.switch_page()

    def start_server(self) -> None:
        self.server_process = multiprocessing.Process(target=start_server)
        self.server_process.start()
        while True:
            if self.__connect_check()["code"] == 200:
                break

    def get_order_id_in_offline_app(self) -> None:
        with open('C:/demo_app/src/ui/api/data.json', 'r') as json_file:
            order_id = json.load(json_file)['order_id']
            self.cart_widget.order_id = order_id if not order_id == 0 else self.cart_widget.set_order_id_in_cart_widget()

    def authorization(self) -> None:
        self.authorization_menu.hide()
        self.user_profile.show()
        self.user_profile.fill_line_edits()

        include_widgets(self, self.__dict__)

    def leave(self) -> None:
        self.authorization_menu.show()
        self.user_profile.hide()
        self.session.leave()
        self.page_list.product_item.switch_page()

        include_widgets(self, self.__dict__)    

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QtWidgets.QMessageBox(parent=self if not parent else parent)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle('Error' if error else 'Information')
        messagebox.setText(text)
        messagebox.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        messagebox.exec_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        with open('C:/demo_app/src/ui/api/data.json', 'w') as json_file:
            json.dump({"order_id": self.cart_widget.order_id}, json_file)
        self.product_list.stop_flag = True
        self.orders_list.stop_flag = True
        self.cart_widget.stop_flag = True
        self.server_process.terminate()
        exit()


