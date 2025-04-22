from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from src import database

class ListarPacientes(QWidget):
    def __init__(self, medico_id):
        super().__init__()
        uic.loadUi("ui/listar_pacientes.ui", self)

        self.medico_id = medico_id
        self.setWindowTitle("Listar Pacientes")

        self.carregar_pacientes()
        self.botaoVoltar.clicked.connect(self.voltar)

    def carregar_pacientes(self):

        pacientes = database.listar_pacientes_por_medico(self.medico_id)
        
        self.tableWidget.setRowCount(len(pacientes))
        self.tableWidget.setColumnCount(2)  # Aqui você pode adicionar mais colunas se necessário

        for row, paciente in enumerate(pacientes):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(paciente[0]))  # Nome
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(paciente[1])))  # Prontuário Eletrônico

    def voltar(self):
        self.close()

