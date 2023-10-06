from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets
from ui.api import resolvers
from src.ui.api.session import Session

session: Session = Session()
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
    def __init__(self) -> None:
        super().__init__()
        if {"code": 400} in self.__connect_check():
            self.show_message(text=self.__connect_check()["msg"], error=True, parent=self)
            

    @resolvers.server_available
    def __connect_check() -> None:
        return None
    

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QtWidgets.QMessageBox(parent=self if not parent else parent)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle('Error' if error else 'Information')
        messagebox.setText(text=text)
        messagebox.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        messagebox.show()