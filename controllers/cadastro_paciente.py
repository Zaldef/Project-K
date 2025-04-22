from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from src import database  # Supondo que as funções de cadastro estão no arquivo database.py


class CadastroPaciente(QWidget):
    def __init__(self, master, medico_id):
        super().__init__()
        uic.loadUi("ui/cadastro_paciente.ui", self)

        self.setWindowTitle("Cadastro de Paciente")
        self.botaoCadastrar.clicked.connect(self.cadastrar_paciente)

        self.master = master
        self.medico_id = medico_id

    def cadastrar_paciente(self):
        # Captura os dados do paciente
        identificacao = self.inputIdentificacao.text().strip()
        prontuario = self.inputProntuario.text().strip()

        # Validação dos campos
        if not identificacao or not prontuario:
            self.labelMensagem.setStyleSheet("color: red;")
            self.labelMensagem.setText("Preencha todos os campos.")
            return

        # Chama a função para cadastrar no banco de dados
        sucesso = database.cadastrar_paciente(identificacao, prontuario, self.medico_id)
        if sucesso:
            self.master.labelMensagem.setStyleSheet("color: green;")
            self.master.labelMensagem.setText("Paciente cadastrado com sucesso!")
            self.master.show()
            self.close()
            
        else:
            self.labelMensagem.setStyleSheet("color: red;")
            self.labelMensagem.setText("Erro ao cadastrar paciente.")
