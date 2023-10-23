from PySide6 import QtWidgets, QtCore, QtGui
from src.ui.orders_widgets.products_list_in_order_form import ProductListInOrder
from src.ui.api.resolvers import get_all_products_in_order, complete_order, get_all_orders


class OrderItem(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()
    
    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        
        self.orderID = QtWidgets.QLabel()
        self.userID = QtWidgets.QLabel()
        self.track_number = QtWidgets.QLabel()
        self.total_cost = QtWidgets.QLabel()
        self.completed = QtWidgets.QLabel()

        self.open_button = QtWidgets.QPushButton()
        self.pick_up_button = QtWidgets.QPushButton()

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.main_h_layout.addWidget(self.orderID)
        self.main_h_layout.addWidget(self.userID)
        self.main_h_layout.addWidget(self.track_number)
        self.main_h_layout.addWidget(self.total_cost)
        self.main_h_layout.addWidget(self.completed)
        self.main_h_layout.addWidget(self.open_button)
        self.main_h_layout.addWidget(self.pick_up_button)

        self.completed.setText('False')

        self.orderID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.track_number.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.completed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.open_button.setText('Open')
        self.pick_up_button.setText('Pick Up!')

        self.open_button.setFixedWidth(50)
        self.pick_up_button.setFixedWidth(50)

        # self.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.orderID.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.userID.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.track_number.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.total_cost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.completed.setFrameShape(QtWidgets.QFrame.Shape.Box)

        # self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.orderID.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.userID.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.track_number.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.total_cost.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.completed.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.setFixedHeight(75)

        self.open_button.clicked.connect(self.on_open_button_click)
        self.pick_up_button.clicked.connect(self.on_pick_up_button_click)


    def set_order_info(self, order_id: int, user_id: int, track_number: str, total_cost: int, completed: bool) -> None:
        self.orderID.setText(str(order_id))
        self.userID.setText(str(user_id))
        self.track_number.setText(str(track_number))
        self.total_cost.setText(str(total_cost))
        self.completed.setText(str(completed))

    def on_pick_up_button_click(self) -> None:
        self.complete_order()

    def complete_order(self) -> None:
        res = complete_order(order_id=int(self.orderID.text()))
        self.parent.parent.show_message(text=res['msg'], error=False if res["code"] == 200 else True, parent=self.parent)
        self.parent.update_orders(get_all_orders(userID=int(self.userID.text()))["result"])

    def on_open_button_click(self) -> None:
        self.open_order_form()

    def open_order_form(self) -> None:
        product_list = ProductListInOrder(self)
        product_list.update_products_in_order(get_all_products_in_order(int(self.orderID.text()))["result"])
        product_list.show()
        