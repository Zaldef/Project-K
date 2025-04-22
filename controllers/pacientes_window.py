from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout, QTableWidget, QLabel
from PyQt5 import uic
from PyQt5.QtCore import Qt
from src import database  

class PacientesWindow(QWidget):
    def __init__(self, medico_id, ver_exames_callback):
        super().__init__()
        uic.loadUi("pacientes_window.ui", self)
        self.medico_id = medico_id
        self.ver_exames_callback = ver_exames_callback  
        self.tabelaPacientes.setColumnWidth(0, 150)
        self.tabelaPacientes.setColumnWidth(1, 250)
        self.tabelaPacientes.setColumnWidth(2, 100)

        self.labelMensagemRodape.setText("")
        self.carregar_pacientes()

    def carregar_pacientes(self):
        self.tabelaPacientes.setRowCount(0)
        pacientes = database.listar_pacientes_por_medico(self.medico_id)

        for row, paciente in enumerate(pacientes):
            prontuario = QTableWidgetItem(str(paciente['prontuario']))
            identificacao = QTableWidgetItem(paciente['identificacao'])

            self.tabelaPacientes.insertRow(row)
            self.tabelaPacientes.setItem(row, 0, prontuario)
            self.tabelaPacientes.setItem(row, 1, identificacao)

            botao_ver = QPushButton("Ver Exames")
            botao_ver.clicked.connect(lambda _, p_id=paciente['id']: self.ver_exames_callback(p_id))
            self.tabelaPacientes.setCellWidget(row, 2, botao_ver)
