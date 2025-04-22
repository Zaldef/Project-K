from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from src import database
from controllers.cadastro_paciente import CadastroPaciente


class Master(QWidget):
    def __init__(self, login_info):

        super().__init__()
        uic.loadUi("ui/master.ui", self)

        self.nome = database.pegar_nome_medico_por_id(login_info)
        self.setWindowTitle("Painel do Médico")
        self.labelBemVindo.setText(f"Bem-vindo, Doutor(a) {self.nome}")
        self.login_info = login_info

        # Conectando os botões às funções
        self.botaoCadastrarPaciente.clicked.connect(self.cadastrar_paciente)
        self.botaoCadastrarExame.clicked.connect(self.cadastrar_exame)
        self.botaoVisualizarGraficos.clicked.connect(self.visualizar_graficos)
        self.botaoGerarRelatorios.clicked.connect(self.gerar_relatorios)
        self.botaoSair.clicked.connect(self.sair)

    def cadastrar_paciente(self):
        self.labelMensagem.setStyleSheet("color: green;")
        self.labelMensagem.setText("Função de cadastro de paciente em construção.")
        self.janela_Cadastrar_Paciente = CadastroPaciente(self, self.login_info)
        self.janela_Cadastrar_Paciente.show()
        self.hide()

    def cadastrar_exame(self):
        self.labelMensagem.setStyleSheet("color: green;")
        self.labelMensagem.setText("Função de cadastro de exame em construção.")

    def visualizar_graficos(self):
        self.labelMensagem.setStyleSheet("color: green;")
        self.labelMensagem.setText("Visualização de gráficos em construção.")

    def gerar_relatorios(self):
        self.labelMensagem.setStyleSheet("color: green;")
        self.labelMensagem.setText("Geração de relatórios em construção.")

    def sair(self):
        self.close()
