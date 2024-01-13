from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtCore
import PySide6.QtWidgets


class UserProfile(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()
    
    def __initUI(self) -> None:
        self.main_h_layout = QtWidgets.QVBoxLayout()
        
        self.user_id_layout = QtWidgets.QHBoxLayout()
        self.access_level_layout = QtWidgets.QHBoxLayout()
        self.login_layout = QtWidgets.QHBoxLayout()
        self.password_layout = QtWidgets.QHBoxLayout()
        self.confirm_layout = QtWidgets.QHBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()

        self.user_id_label = QtWidgets.QLabel()
        self.access_level_label = QtWidgets.QLabel()
        self.login_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.confirm_label = QtWidgets.QLabel()

        self.user_id_line_edit = QtWidgets.QLineEdit()
        self.access_level_line_edit = QtWidgets.QLineEdit()
        self.login_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.confirm_line_edit = QtWidgets.QLineEdit()

        self.leave_button = QtWidgets.QPushButton()
        self.edit_button = QtWidgets.QPushButton()
        self.allow_button = QtWidgets.QPushButton()

        self.spacer = QtWidgets.QSpacerItem(0, 10)

    def __settingUI(self) -> None:
        self.setLayout(self.main_h_layout)

        self.main_h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.setMaximumWidth(250)

        self.main_h_layout.addLayout(self.user_id_layout)
        self.main_h_layout.addLayout(self.access_level_layout)
        self.main_h_layout.addSpacerItem(self.spacer)
        self.main_h_layout.addLayout(self.login_layout)
        self.main_h_layout.addLayout(self.password_layout)
        self.main_h_layout.addLayout(self.confirm_layout)
        self.main_h_layout.addSpacerItem(self.spacer)
        self.main_h_layout.addLayout(self.button_layout)

        self.user_id_layout.addWidget(self.user_id_label)
        self.access_level_layout.addWidget(self.access_level_label)
        self.login_layout.addWidget(self.login_label)
        self.password_layout.addWidget(self.password_label)
        self.confirm_layout.addWidget(self.confirm_label)

        self.user_id_layout.addWidget(self.user_id_line_edit)
        self.access_level_layout.addWidget(self.access_level_line_edit)
        self.login_layout.addWidget(self.login_line_edit)
        self.password_layout.addWidget(self.password_line_edit)
        self.confirm_layout.addWidget(self.confirm_line_edit)

        self.button_layout.addWidget(self.leave_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.allow_button)

        self.leave_button.setText('Leave')
        self.edit_button.setText('Edit')
        self.allow_button.setText('Allow')

        self.user_id_label.setText('UserID: ')
        self.access_level_label.setText('Access level')
        self.login_label.setText('Login: ')
        self.password_label.setText('Password: ')
        self.confirm_label.setText('Confirm: ')

        self.user_id_line_edit.setEnabled(False)
        self.access_level_line_edit.setEnabled(False)
        self.login_line_edit.setEnabled(False)

        self.login_line_edit.setFixedWidth(150)
        self.password_line_edit.setFixedWidth(150)
        self.confirm_line_edit.setFixedWidth(150)
        self.user_id_line_edit.setFixedWidth(150)
        self.access_level_line_edit.setFixedWidth(150)

        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.set_line_edit_enable(False)

        self.allow_button.setEnabled(False)

        self.leave_button.clicked.connect(self.on_leave_click)
        self.edit_button.clicked.connect(self.on_edit_click)
        self.allow_button.clicked.connect(self.on_allow_click)

    def set_line_edit_enable(self, enabled: bool) -> None:
        self.confirm_line_edit.setEnabled(enabled)
        self.password_line_edit.setEnabled(enabled)

    def fill_line_edits(self) -> None:
        self.user_id_line_edit.setText(str(self.parent.session.user.userID))
        self.access_level_line_edit.setText(str(self.parent.session.user.access_level))
        self.login_line_edit.setText(str(self.parent.session.user.login))  

    def on_leave_click(self) -> None:
        if QtWidgets.QMessageBox.question(self, 'Info', 'Are you sure?') != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        self.parent.leave()

    def on_edit_click(self) -> None:
        self.edit_button.setEnabled(False)
        self.allow_button.setEnabled(True)

        self.set_line_edit_enable(True)

    def validate_password(self) -> bool:
        for x in (self.password_line_edit.text(), self.confirm_line_edit.text()):
            if x == '':
                return False
        return self.password_line_edit.text() == self.confirm_line_edit.text()

    def on_allow_click(self) -> None:

        if not self.validate_password():
            return self.parent.show_message(
                text='Incorrect confirm password or one or more fields is empty',
                error=True,
                parent=self
            )
        
        self.parent.session.update(password=self.password_line_edit.text())

        if self.parent.session.error:
            return self.parent.show_message(
                text=self.parent.session.error,
                error=True,
                parent=self
            )

        self.set_line_edit_enable(False)
        self.password_line_edit.setText('')
        self.confirm_line_edit.setText('')
        self.allow_button.setEnabled(False)
        self.edit_button.setEnabled(True)
