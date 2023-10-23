from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_widgets.tools import get_pixmap_path, include_widgets
from ui.api.resolvers import get_all_orders, get_order
from ui.orders_widgets.order_item import OrderItem
import threading


class OrdersList(QtWidgets.QWidget):
    stop_flag = None
    add_order_signal: QtCore.Signal = QtCore.Signal(int, int, str, int, bool)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.order_search_line_edit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

        self.statuslabel = OrderItem(self)

    def __settingUI(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_h_layout.setContentsMargins(10, 10, 10, 0)
        self.main_v_layout.addLayout(self.tools_h_layout)
        self.main_v_layout.addWidget(self.scroll_area)
        self.tools_h_layout.addWidget(self.order_search_line_edit)
        self.tools_h_layout.addWidget(self.search_button)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_layout.addWidget(self.statuslabel)

        self.statuslabel.set_order_info('OrderID', 'UserID', 'Track-number', 'Total cost', 'Completed')
        self.statuslabel.open_button.setProperty('access_level', 10)
        self.statuslabel.pick_up_button.setProperty('access_level', 10)

        self.search_button.setIcon(QtGui.QPixmap(get_pixmap_path("search.png")))
        self.search_button.setFixedSize(24, 24)
        self.search_button.setProperty("access_level", 0)
        self.order_search_line_edit.setProperty("access_level", 0)

        self.search_button.clicked.connect(self.on_find_button_click)
        self.add_order_signal.connect(self.add_order_slot)
    
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return.numerator:
            self.on_find_button_click()

    def on_find_button_click(self) -> None:
        orders = get_order(self.order_search_line_edit.text(), self.parent.session.user.userID)["result"]
        self.update_orders(orders)

    def update_orders(self, orders) -> None:
        self.clear_orders()
        if orders:
            threading.Thread(target=lambda: self.load_orders(orders)).start()

    def load_orders(self, orders) -> None:
        for order in [orders] if type(orders) == dict else orders:
            if self.stop_flag:
                exit()

            self.add_order_signal.emit(
                order["ID"],
                order["accountID"],
                order["track_number"],
                order["total_cost"],
                order["completed"]
            )

    def add_order(self, order_id: int, user_id: int, track_number: str, total_cost: int, completed: bool) -> None:
        new_order = OrderItem(self)
        self.scroll_widget.__dict__.update({order_id: new_order})
        new_order.set_order_info(order_id=str(order_id), user_id=str(user_id), track_number=str(track_number), total_cost=str(total_cost), completed=str(completed))
        self.scroll_layout.addWidget(new_order)
        include_widgets(main_win=self.parent, elements=self.__dict__)
    
    def clear_orders(self) -> None:
        for product in dict(self.scroll_widget.__dict__):
            if type(self.scroll_widget.__dict__[product]) == OrderItem:
                self.scroll_widget.__dict__[product].close()
                self.scroll_widget.__dict__.pop(product)

    QtCore.Slot(int, int, str, int, bool)
    def add_order_slot(self, order_id: int, user_id: int, track_number: str,  total_cost: int, completed: bool) -> None:
        self.add_order(order_id=order_id, user_id=user_id, track_number=track_number, total_cost=total_cost, completed=completed)
        include_widgets(main_win=self.parent, elements=self.__dict__)