from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtCore
import PySide6.QtWidgets
from ui.register_form import RegisterWindow
from ui.login_form import LoginWindow


class AuthorizationMenu(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()

    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.login_button = QtWidgets.QPushButton()
        self.register_button = QtWidgets.QPushButton()
        
    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setMaximumWidth(120)

        self.main_h_layout.addWidget(self.login_button)
        self.main_h_layout.addWidget(self.register_button)
        
        self.main_h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.login_button.setText('Login')
        self.register_button.setText('Register')

        self.login_button.clicked.connect(self.on_log_button_click)
        self.register_button.clicked.connect(self.on_reg_button_click)

    def on_log_button_click(self) -> None:
        self.open_login_dialog()

    def open_login_dialog(self) -> None:
        LoginWindow(self.parent)

    def on_reg_button_click(self) -> None:
        self.open_register_dialog()
 
    def open_register_dialog(self) -> None:
        RegisterWindow(self.parent)