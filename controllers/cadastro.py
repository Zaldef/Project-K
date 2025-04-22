from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from src import database


class Cadastro(QWidget):
    def __init__(self, login):
        super().__init__()
        uic.loadUi("ui/cadastro.ui", self)

        self.setWindowTitle("Cadastro")
        self.botaoCadastrar.clicked.connect(self.cadastrar)
        self.botaoVoltar.clicked.connect(self.voltar)

        self.login = login

    def cadastrar(self):
        login = self.inputLogin.text().strip()
        senha = self.inputSenha.text().strip()
        nome = self.inputNome.text().strip()

        if not login or not senha or not nome:
            self.labelMensagem.setStyleSheet("color: red;")
            self.labelMensagem.setText("Preencha todos os campos para cadastrar.")
        else:
            sucesso = database.cadastrar_medico(login, senha, nome)
            if sucesso:
                self.login.labelMensagem.setStyleSheet("color: green;")
                self.login.labelMensagem.setText("Cadastro realizado com sucesso.")
                self.close()
                self.login.show()
            else:
                self.labelMensagem.setStyleSheet("color: red;")
                self.labelMensagem.setText("Usuário já existe.")
                
    def voltar(self):
        self.close()
        self.login.show()
