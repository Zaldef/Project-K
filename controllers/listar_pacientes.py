from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt5 import uic
from src import database
from controllers.perfil_paciente import PerfilPaciente

class ListarPacientes(QWidget):
    def __init__(self, medico_id, master):
        super().__init__()
        uic.loadUi("ui/listar_pacientes.ui", self)

        self.master = master
        self.medico_id = medico_id
        self.setWindowTitle("Listar Pacientes")

        self.carregar_pacientes()
        self.botaoVoltar.clicked.connect(self.voltar)

    def carregar_pacientes(self):

        pacientes = database.listar_pacientes_por_medico(self.medico_id)
        
        self.tableWidget.setRowCount(len(pacientes))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # precisa importar isso

        for row, paciente in enumerate(pacientes):
            self.tableWidget.setRowHeight(row, 60)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(paciente[1]))  # Nome
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(paciente[2])))  # Prontuário Eletrônico

            widget_botao = QWidget()
            layout_botao = QHBoxLayout()

            botao1 = QPushButton("Ver perfil")
            botao1.clicked.connect(lambda _, pid=paciente[0]: self.ver_perfil_paciente(pid))
            layout_botao.addWidget(botao1)

            botao2 = QPushButton("Editar")
            botao2.clicked.connect(lambda _, pid=paciente[0]: self.editar_paciente(pid))
            layout_botao.addWidget(botao2)

            botao3 = QPushButton("Excluir")
            botao3.clicked.connect(lambda _, pid=paciente[0]: self.excluir_paciente(pid))
            layout_botao.addWidget(botao3)

            widget_botao.setLayout(layout_botao)
            self.tableWidget.setCellWidget(row, 2, widget_botao)

    def ver_perfil_paciente(self, paciente_id):
        self.perfil_paciente = PerfilPaciente(paciente_id, self.master)
        self.perfil_paciente.show()
        self.close()

    def editar_paciente(self, paciente_id):
        # Aqui você pode implementar a lógica para editar o paciente
        print(f"Editar paciente com ID: {paciente_id}")
    
    def excluir_paciente(self, paciente_id):
        # Aqui você pode implementar a lógica para excluir o paciente
        print(f"Excluir paciente com ID: {paciente_id}")

    def voltar(self):
        self.close()
        self.master.show()


