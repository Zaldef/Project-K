from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from src import database


class Cadastro(QWidget):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("ui/cadastro.ui", self)
        self.parent = parent
        
        self.setWindowTitle("Cadastro")
        self.botaoCadastrar.clicked.connect(self.cadastrar)
        self.botaoVoltar.clicked.connect(self.voltar)

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
                QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso.")
                self.close()
                self.parent.show()
            else:
                QMessageBox.warning(self, "Erro", "Erro ao cadastrar médico.")
                
    def voltar(self):
        self.close()
        self.parent.show()
