from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from settings_window import SettingsWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi(r"D:\dev\client_side\ui\login_window.ui", self)

        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.open_settings_window)

        self.show()

    def go_to_register_page(self):
        print("Go To register Page")

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.displayInfo()
        self.close()

        print("Go To Settings Window")
