from PySide6.QtWidgets import QApplication
import sys
from ui.main_widgets.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = MainWindow()
    app.exec()