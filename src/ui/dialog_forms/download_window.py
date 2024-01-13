from PySide6 import QtWidgets, QtCore, QtGui


class DownloadWindow(QtWidgets.QSplashScreen):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.__init_ui()
        self.__setup_ui()
        self.show()
    
    def __init_ui(self) -> None:
        self.main_h_layout = QtWidgets.QVBoxLayout()
        self.status_bar = QtWidgets.QProgressBar()
        self.label = QtWidgets.QLabel()
        self.spacer = QtWidgets.QSpacerItem(0, 15)
    
    def __setup_ui(self) -> None:
        self.resize(285, 150)
        self.setLayout(self.main_h_layout)
        self.main_h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label.setText('Wait please...')
        self.status_bar.setStyleSheet('QProgressBar{border: 2px solid #2196F3, background-color: #00ff00;}')

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.main_h_layout.addWidget(self.status_bar)
        self.main_h_layout.addSpacerItem(self.spacer)
        self.main_h_layout.addWidget(self.label)

    def set_value_for_progress_bar(self, value: int):
        self.status_bar.setValue(value)