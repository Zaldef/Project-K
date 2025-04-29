from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from src import database  # Supondo que as funções de cadastro estão no arquivo database.py


class CadastroPaciente(QWidget):
    def __init__(self, parent, medico_id, mode):
        super().__init__()
        uic.loadUi("ui/cadastro_paciente.ui", self)
        self.mode = mode
        self.setWindowTitle("Cadastro de Paciente")
        self.botaoCadastrar.clicked.connect(self.cadastrar_paciente)

        self.parent = parent
        self.medico_id = medico_id

        self.botaoVoltar.clicked.connect(self.voltar)

    def cadastrar_paciente(self):
        # Captura os dados do paciente
        identificacao = self.inputIdentificacao.text().strip()
        prontuario = self.inputProntuario.text().strip()

        # Validação dos campos
        if not identificacao or not prontuario:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
        

        # Chama a função para cadastrar no banco de dados
        sucesso = database.cadastrar_paciente(prontuario, identificacao, self.medico_id)
        if sucesso:
            QMessageBox.information(self, "Sucesso", "Paciente cadastrado com sucesso.")
            if self.mode == 1:
                self.parent.carregar_pacientes()
            self.voltar()
        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar paciente.")
    
    def voltar(self):
        self.close()
        self.parent.show()
