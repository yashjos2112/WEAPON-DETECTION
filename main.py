from PyQt5.QtWidgets import QApplication
import sys
from login_window import LoginWindow

app = QApplication(sys.argv)  # on whcih application system will run
mainwindow = LoginWindow()

try:
    sys.exit(app.exec_())
except:
    print("Exeting")
