from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5 import uic

from controllers.master import Master
from controllers.cadastro import Cadastro
from src import database


class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        # Conecta botões aos métodos
        self.botaoEntrar.clicked.connect(self.entrar)
        self.botaoCadastrar.clicked.connect(self.cadastrar)

    def entrar(self):
        login = self.inputLogin.text()
        senha = self.inputSenha.text()

        if not login or not senha:
            self.labelMensagem.setStyleSheet("color: red;")
            self.labelMensagem.setText("Preencha todos os campos.")
            self.inputLogin.clear()
            self.inputSenha.clear()
        else:
            sucesso, id = database.verificar_login(login, senha)
            if sucesso:
                self.janela_principal = Master(id)
                self.janela_principal.show()
                self.close()
            else:
                self.labelMensagem.setStyleSheet("color: red;")
                self.labelMensagem.setText("Login ou senha inválidos.")
    
    def cadastrar(self):
        self.janela_cadastro = Cadastro(self)
        self.janela_cadastro.show()
        self.hide()
