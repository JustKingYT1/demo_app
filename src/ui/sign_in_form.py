from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from src.ui.api.session import Session


class SignWindow(QtWidgets.QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.__initUI()
        self.__settingUI()
        self.show()

    
    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()

        self.labels_h_layout = QtWidgets.QHBoxLayout()
        self.line_edits_h_layout = QtWidgets.QHBoxLayout()

        self.label_fio = QtWidgets.QLabel()

        self.line_edit_fio = QtWidgets.QLineEdit()

        self.confirm_button = QtWidgets.QPushButton()

    
    def __settingUI(self) -> None:
        self.setWindowTitle("Sign in")

        self.setLayout(self.main_v_layout)

        self.labels_h_layout.addWidget(self.label_fio)
        self.line_edits_h_layout.addWidget(self.line_edit_fio)

        self.main_v_layout.addLayout(self.labels_h_layout)
        self.main_v_layout.addLayout(self.line_edits_h_layout)
        self.main_v_layout.addWidget(self.confirm_button)
        
        self.label_fio.setText("FIO")
        self.confirm_button.setText("Confirm")

        self.confirm_button.clicked.connect(self.on_click_confirm_button )

    
    def data_is_valid(self) -> bool:
        if self.line_edit_fio.text() == "":
            self.parent().show_message(text="Field FIO is empty!", error=True, parent=self)
            return False
        
        return True
    
    def on_click_confirm_button(self) -> None:
        self.sign()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key == QtCore.Qt.Key.Key_Return:
            self.sign()

    
    def sign(self) -> None:
        if not self.data_is_valid():
            return

        self.parent().session.sign(FIO=self.line_edit_fio.text())

        if self.parent().session.error:
            self.parent().show_message(text=self.parent().session.error, error=True, parent=self)
            return
        
        self.parent().show_message(text=f"Hello {self.line_edit_fio.text()}!", parent=self)

        self.hide()
    

