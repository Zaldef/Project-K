import sys
from PyQt5.QtWidgets import QApplication 
from controllers.login import Login
from src.database import inicializar_banco

from controllers.master import Master

def main():
    inicializar_banco()

    app = QApplication(sys.argv)
    #initial_page = Master(1)  # Passando um ID de médico fictício para inicializar a tela principal
    #initial_page.show()
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()