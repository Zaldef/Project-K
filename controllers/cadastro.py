from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from src import database


class Cadastro(QWidget):
    def __init__(self, login_window):
        super().__init__()
        uic.loadUi("ui/cadastro_window.ui", self)

        self.setWindowTitle("Cadastro")
        self.botaoCadastrar.clicked.connect(self.cadastrar)

        self.login_window = login_window

    def cadastrar(self):
        login = self.inputLogin.text().strip()
        senha = self.inputSenha.text().strip()
        nome = self.inputNome.text().strip()

        if not login or not senha or not nome:
            self.labelMensagem.setStyleSheet("color: red;")
            self.labelMensagem.setText("Preencha login e senha para cadastrar.")
        else:
            sucesso = database.cadastrar_medico(login, senha, nome)
            if sucesso:
                self.login_window.labelMensagem.setStyleSheet("color: green;")
                self.login_window.labelMensagem.setText("Cadastro realizado com sucesso.")
                self.close()
                self.login_window.show()
            else:
                self.login_windowlabelMensagem.setStyleSheet("color: red;")
                self.login_windowlabelMensagem.setText("Login já existe.")
                self.close()
                self.login_window.show()
