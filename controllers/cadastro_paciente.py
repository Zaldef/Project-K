from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from src import database  # Supondo que as funções de cadastro estão no arquivo database.py


class CadastroPaciente(QWidget):
    def __init__(self, ante, medico_id, mode):
        super().__init__()
        uic.loadUi("ui/cadastro_paciente.ui", self)

        self.setWindowTitle("Cadastro de Paciente")
        self.botaoCadastrar.clicked.connect(self.cadastrar_paciente)

        self.mode = mode # 1 para listar_pacientes, 0 para master
        self.ante = ante # objeto (tela) que chamou essa tela
        self.medico_id = medico_id

        self.botaoVoltar.clicked.connect(self.voltar)

    def cadastrar_paciente(self):
        # Captura os dados do paciente
        identificacao = self.inputIdentificacao.text().strip()
        prontuario = self.inputProntuario.text().strip()

        # Validação dos campos
        if not identificacao or not prontuario:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        # Chama a função para cadastrar no banco de dados
        sucesso = database.cadastrar_paciente(prontuario, identificacao, self.medico_id)
        if sucesso:
            QMessageBox.information(self, "Sucesso", "Paciente cadastrado com sucesso.")
            if self.mode == 1:
                self.ante.carregar_pacientes()
                self.ante.show()
                self.close()
            else:
                self.ante.show()
                self.close()
            
        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar paciente. Verifique os dados e tente novamente.")
    
    def voltar(self):
        self.close()
        self.ante.show()
