from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui


class LoginWindow(QtWidgets.QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        print(parent)
        self.parent = parent
        self.__initUI()
        self.__settingUI()
        self.show()

    def __initUI(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.label_line_edit_h_layout = QtWidgets.QHBoxLayout()
        self.label_v_layout = QtWidgets.QVBoxLayout()
        self.line_edit_v_layout = QtWidgets.QVBoxLayout()

        self.label_userID = QtWidgets.QLabel()
        self.label_login = QtWidgets.QLabel()
        self.label_password = QtWidgets.QLabel()

        self.spacer = QtWidgets.QSpacerItem(0, 10)

        self.line_edit_userID = QtWidgets.QLineEdit()
        self.line_edit_login = QtWidgets.QLineEdit()
        self.line_edit_password = QtWidgets.QLineEdit()

        self.login_button = QtWidgets.QPushButton()

    
    def __settingUI(self) -> None:
        self.setWindowTitle("Log in")

        self.setLayout(self.main_v_layout)
        self.main_v_layout.addLayout(self.label_line_edit_h_layout)
        self.label_line_edit_h_layout.addLayout(self.label_v_layout)
        self.label_line_edit_h_layout.addLayout(self.line_edit_v_layout)

        self.label_v_layout.addWidget(self.label_userID)
        self.label_v_layout.addSpacerItem(self.spacer)
        self.label_v_layout.addWidget(self.label_login)
        self.label_v_layout.addWidget(self.label_password)

        self.line_edit_v_layout.addWidget(self.line_edit_userID)
        self.line_edit_v_layout.addSpacerItem(self.spacer)
        self.line_edit_v_layout.addWidget(self.line_edit_login)
        self.line_edit_v_layout.addWidget(self.line_edit_password)

        self.main_v_layout.addWidget(self.login_button)

        self.label_userID.setText("User ID")
        self.label_login.setText("Login")
        self.label_password.setText("Password")

        self.login_button.setText("Log in")

        self.line_edit_userID.setReadOnly(True)

        self.line_edit_userID.setText(str(self.parent.session.user.userID))
       
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.login_button.clicked.connect(self.on_login_button_clicked)

    
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.log_in()
    
    def data_is_valid(self) -> bool:
        for x in (self.line_edit_login, self.line_edit_password):
            if x.text() == "":
                self.parent().show_message(text="One or more fields are empty", error=True, parent=self)
                return False
            
        return True

    def on_login_button_clicked(self) -> None:
        self.log_in()

    def log_in(self) -> None:
        if not self.data_is_valid():
            return
        
        self.parent.session.login(login=self.line_edit_login.text(), password=self.line_edit_password.text())
        
        if self.parent.session.error:
            return self.parent.show_message(
                text=self.parent.session.error,
                error=True,
                parent=self
            )

        if self.parent.session.auth:
            self.parent.show_message(
                text='Successful login',
                error=False,
                parent=self
            )

        self.parent.authorization()

        self.close()
        