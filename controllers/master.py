from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from src import database
from controllers.cadastro_paciente import CadastroPaciente
from controllers.listar_pacientes import ListarPacientes
from controllers.cadastro_exame import CadastroExame
from controllers.visualizar_grafico import VisualizarGraficos


class Master(QWidget):
    def __init__(self, medico_id):
        super().__init__()
        uic.loadUi("ui/master.ui", self)
        self.setWindowTitle("Painel do Médico")

        self.prox = None
        self.nome = database.pegar_nome_medico_por_id(medico_id)
        self.labelBemVindo.setText(f"Bem-vindo, Doutor(a) {self.nome}")
        self.medico_id = medico_id
        self.paciente_id = 1

        self.botaoListarPacientes.clicked.connect(self.listar_pacientes)
        self.botaoCadastrarPaciente.clicked.connect(self.cadastrar_paciente)
        self.botaoCadastrarExame.clicked.connect(self.cadastrar_exame)
        self.botaoVisualizarGraficos.clicked.connect(self.visualizar_graficos)
        self.botaoGerarRelatorios.clicked.connect(self.gerar_relatorios)
        self.botaoSair.clicked.connect(self.sair)


    def listar_pacientes(self):
        self.prox = ListarPacientes(self.medico_id, self)
        self.prox.show()
        self.hide()

    def cadastrar_paciente(self):
        self.prox = CadastroPaciente(self, self.medico_id, 0)
        self.prox.show()
        self.hide()

    def cadastrar_exame(self):
        self.prox = CadastroExame(1, self.medico_id, self) # Aqui você pode passar o ID do paciente que deseja cadastrar o exame
        self.prox.show()
        self.hide()

    def visualizar_graficos(self):
        self.prox = VisualizarGraficos("paciente1_20250429170307")  # Aqui você pode passar o ID do exame que deseja visualizar
        self.prox.show()
        self.hide()

    def gerar_relatorios(self):
        QMessageBox.warning(self, "Erro", "Funcionalidade não implementada.")

    def sair(self):
        self.close()
