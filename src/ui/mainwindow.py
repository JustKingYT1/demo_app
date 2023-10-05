from PySide6 import QtCore, QtWidgets, QtGui
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