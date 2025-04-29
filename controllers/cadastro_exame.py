import os
import shutil
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QDateTime
from PyQt5 import uic
from src import database

class CadastroExame(QWidget):
    def __init__(self, paciente_id, medico_id, parent):
        super().__init__()
        uic.loadUi("ui/cadastro_exame.ui", self)

        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.parent_ref = parent
        self.caminho_csv = None
        self.inputData.setDateTime(QDateTime.currentDateTime())
        self.setWindowTitle("Cadastrar Exame")

        # Conectando botões
        self.botaoSelecionarCSV.clicked.connect(self.selecionar_csv)
        self.botaoCadastrar.clicked.connect(self.cadastrar_exame)
        self.botaoVoltar.clicked.connect(self.voltar)

    def selecionar_csv(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Selecionar CSV", "", "Arquivos CSV (*.csv)")
        if caminho:
            self.caminho_csv_temp = caminho
            nome_arquivo = os.path.basename(caminho)
            self.labelCSVSelecionado.setText(f"CSV selecionado: {nome_arquivo}")

    def cadastrar_exame(self):
        data = self.inputData.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        descricao = self.inputDescricao.toPlainText()

        if not data or not descricao or not self.caminho_csv_temp:
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha todos os campos obrigatórios e selecione um CSV.")
            return

        # Define nome do arquivo destino (ainda não copia)
        nome_arquivo = f"paciente{self.paciente_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        pasta_destino = os.path.join("exames", "csvs")
        os.makedirs(pasta_destino, exist_ok=True)
        destino_completo = os.path.join(pasta_destino, nome_arquivo)

        try:
            # Primeiro, insere no banco de dados
            database.inserir_exame(
                self.paciente_id,
                self.medico_id,
                data,
                descricao,
                destino_completo  # Caminho final do CSV será salvo no banco
            )

            # Agora sim copia o arquivo CSV
            shutil.copy(self.caminho_csv_temp, destino_completo)

            QMessageBox.information(self, "Sucesso", "Exame cadastrado com sucesso.")
            self.close()
            self.parent_ref.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar exame:\n{str(e)}")

    def voltar(self):
        self.close()
        self.parent_ref.show()
