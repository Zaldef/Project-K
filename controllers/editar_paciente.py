from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from src import database

class EditarPaciente(QWidget):
    def __init__(self, paciente_id, parent):
        super().__init__()
        uic.loadUi("ui/editar_paciente.ui", self)

        self.paciente_id = paciente_id
        self.parent = parent
        self.setWindowTitle("Editar Paciente")

        self.carregar_dados_paciente()
        self.botaoSalvar.clicked.connect(self.salvar)
        self.botaoCancelar.clicked.connect(self.voltar)

    def carregar_dados_paciente(self):
        dados = database.obter_dados_paciente(self.paciente_id)
        if dados:
            self.inputNome.setText(dados[0])
            self.inputProntuario.setText(str(dados[1]))

    def salvar(self):
        nome = self.inputNome.text().strip()
        prontuario = self.inputProntuario.text().strip()

        if nome and prontuario:
            database.atualizar_paciente(self.paciente_id, nome, prontuario)
            QMessageBox.information(self, "Sucesso", "Paciente atualizado com sucesso.")
            self.voltar()
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")

    def voltar(self):
        self.close()
        self.parent.carregar_pacientes()
        self.parent.show()
