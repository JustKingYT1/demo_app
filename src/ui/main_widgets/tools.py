from src.settings import IMAGE_DIR
from PySide6 import QtWidgets


def get_pixmap_path(pixmap: str) -> str:
    return f'{IMAGE_DIR}/{pixmap}'

def include_widgets(main_win, elements: dict[str, QtWidgets.QWidget], count: int = 0):
    for key, item in elements.items():
        if not issubclass(type(item), QtWidgets.QWidget) or issubclass(type(item), QtWidgets.QMainWindow):
            count += 1
            continue

        if item.property('access_level') is not None:
            item.show() if main_win.session.user.access_level >= item.property('access_level') else item.hide()
        if count < 50:
            include_widgets(main_win=main_win, elements=item.__dict__, count=count)