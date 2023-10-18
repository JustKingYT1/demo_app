from PySide6 import QtWidgets, QtCore, QtGui


class OrderItem(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
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

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.main_h_layout.addWidget(self.orderID)
        self.main_h_layout.addWidget(self.userID)
        self.main_h_layout.addWidget(self.track_number)
        self.main_h_layout.addWidget(self.total_cost)
        self.main_h_layout.addWidget(self.completed)
        self.main_h_layout.addWidget(self.open_button)

        self.completed.setText('False')

        self.orderID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.track_number.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.completed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        
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


    def set_order_info(self, order_id: int, user_id: int, track_number: str, total_cost: int, completed: bool) -> None:
        self.orderID.setText(str(order_id))
        self.userID.setText(str(user_id))
        self.track_number.setText(str(track_number))
        self.total_cost.setText(str(total_cost))
        self.completed.setText(str(completed))

    def on_open_button_click(self) -> None:
        self.open_order_form()

    def open_order_form(self) -> None:
        pass
