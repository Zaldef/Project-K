import sys
from PyQt5.QtWidgets import QApplication 
from controllers.login import Login
from src.database import inicializar_banco

def main():
    inicializar_banco()

    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
