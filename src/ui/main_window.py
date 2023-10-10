from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets
from ui.api import resolvers
from src.ui.api.session import Session
from ui.sign_in_form import SignWindow
from ui.register_form import RegisterWindow
from ui.login_form import LoginWindow

main_win = None

def include_widgets(elements: dict[str, QtWidgets.QWidget]):
    global session

    for key, item in elements.items():
        if not issubclass(type(item), QtWidgets.QWidget):
            continue

        if item.property('access_level') is not None:
            item.show() if session.user.access_level >= item.property('access_level') else item.hide()

        include_widgets(item.__dict__)


class MainWindow(QtWidgets.QMainWindow):
    session: Session = Session()

    def __init__(self) -> None:
        super().__init__()
        self.__initUI()
        self.__settingUI()
        if self.__connect_check():
            if self.__connect_check()["code"] == 400:
                self.show_message(text=self.__connect_check()["msg"], error=True, parent=self)
                exit()
        

        sign_window = SignWindow(self)
        sign_window.show()
        sign_window.exec_()

        if self.session.user.userID == -1:
            exit()

        self.show()
            
    @staticmethod
    @resolvers.server_available
    def __connect_check() -> None:
        return None
    

    def __initUI(self) -> None:
        self.central_widget = QtWidgets.QWidget()

        self.main_h_layout = QtWidgets.QHBoxLayout()

        self.log_in_button = QtWidgets.QPushButton()
        self.sign_up_button = QtWidgets.QPushButton()


    def __settingUI(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)
        self.main_h_layout.addWidget(self.log_in_button)
        self.main_h_layout.addWidget(self.sign_up_button)

        self.log_in_button.setText("Log in!")
        self.sign_up_button.setText("Sign up!")

        self.log_in_button.clicked.connect(self.open_login_dialog)
        self.sign_up_button.clicked.connect(self.open_register_dialog)

    def open_login_dialog(self) -> None:
        LoginWindow(self)

    def open_register_dialog(self) -> None:
        RegisterWindow(self)
    

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QtWidgets.QMessageBox(parent=self if not parent else parent)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle('Error' if error else 'Information')
        messagebox.setText(text)
        messagebox.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        messagebox.show()
        messagebox.exec_()