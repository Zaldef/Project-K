from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QPushButton, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from src import database  # Presumindo que você vá adicionar um método de listar exames por paciente

class PerfilPaciente(QWidget):
    def __init__(self, paciente_id, parent):
        super().__init__()
        uic.loadUi("ui/perfil_paciente.ui", self)

        self.paciente_id = paciente_id
        self.parent = parent
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
        exames = database.listar_exames_por_paciente(self.paciente_id)

        self.tableWidget.setRowCount(len(exames))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Data", "Descrição", "Ações"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        for row, exame in enumerate(exames):
            data_exame = exame[0]  # Ex: '2025-04-24 14:30'
            descricao = exame[1]
            caminho_csv = exame[2]

            self.tableWidget.setItem(row, 0, QTableWidgetItem(data_exame))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(descricao))

            botao_download = QPushButton("Baixar CSV")
            botao_download.clicked.connect(lambda _, caminho=caminho_csv: QDesktopServices.openUrl(QUrl.fromLocalFile(caminho)))
            self.tableWidget.setCellWidget(row, 2, botao_download)

    def voltar(self):
        self.close()
        self.parent.show()
