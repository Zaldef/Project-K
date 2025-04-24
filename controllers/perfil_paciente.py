from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from src import database  # Presumindo que você vá adicionar um método de listar exames por paciente

class PerfilPaciente(QWidget):
    def __init__(self, paciente_id, master):
        super().__init__()
        uic.loadUi("ui/perfil_paciente.ui", self)

        self.paciente_id = paciente_id
        self.master = master
        self.setWindowTitle("Perfil do Paciente")

        self.carregar_dados_paciente()
        self.carregar_exames()

        self.botaoVoltar.clicked.connect(self.voltar)

    def carregar_dados_paciente(self):
        dados = database.obter_dados_paciente(self.paciente_id)
        if dados:
            nome, prontuario = dados
            self.labelNome.setText(f"Nome: {nome}")
            self.labelProntuario.setText(f"Prontuário: {prontuario}")
        else:
            self.labelNome.setText("Nome: Não encontrado")
            self.labelProntuario.setText("Prontuário: Não encontrado")

    def carregar_exames(self):
        # Quando você implementar, troque essa linha:
        exames = []  # <- Coloque aqui a consulta: database.listar_exames_por_paciente(self.paciente_id)

        self.tableExames.setRowCount(len(exames))
        self.tableExames.setColumnCount(3)
        self.tableExames.horizontalHeader().setStretchLastSection(True)
        self.tableExames.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # precisa importar isso

        for row, exame in enumerate(exames):
            data, tipo, descricao = exame
            self.tableExames.setItem(row, 0, QTableWidgetItem(data))
            self.tableExames.setItem(row, 1, QTableWidgetItem(tipo))
            self.tableExames.setItem(row, 2, QTableWidgetItem(descricao))

    def voltar(self):
        self.close()
        self.master.show()
