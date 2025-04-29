from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QMessageBox, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5 import uic
import shutil
import os
from src import database
from functools import partial

class PerfilPaciente(QWidget):
    def __init__(self, paciente_id, ante):
        super().__init__()
        uic.loadUi("ui/perfil_paciente.ui", self)

        self.paciente_id = paciente_id
        self.ante = ante
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

        self.tableExames.setRowCount(len(exames))
        self.tableExames.setColumnCount(3)
        self.tableExames.setHorizontalHeaderLabels(["Data", "Descrição", "Ações"])
        self.tableExames.horizontalHeader().setStretchLastSection(True)
        self.tableExames.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row, exame in enumerate(exames):
            id_exame, data, arquivo_csv, descricao = exame

            self.tableExames.setItem(row, 0, QTableWidgetItem(data))
            self.tableExames.setItem(row, 1, QTableWidgetItem(descricao))

            # Botões de ação
            botoes_widget = QWidget()
            layout = QHBoxLayout(botoes_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(Qt.AlignCenter)

            btn_editar = QPushButton("✏️")
            btn_editar.setToolTip("Editar exame")
            btn_editar.clicked.connect(partial(self.editar_exame, id_exame))

            btn_baixar = QPushButton("⬇️")
            btn_baixar.setToolTip("Baixar CSV")
            btn_baixar.clicked.connect(partial(self.baixar_exame, arquivo_csv))

            btn_excluir = QPushButton("🗑️")
            btn_excluir.setToolTip("Excluir exame")
            btn_excluir.clicked.connect(partial(self.excluir_exame, id_exame, arquivo_csv))

            layout.addWidget(btn_editar)
            layout.addWidget(btn_baixar)
            layout.addWidget(btn_excluir)

            self.tableExames.setCellWidget(row, 2, botoes_widget)

    def editar_exame(self, id_exame):
        QMessageBox.information(self, "Editar", f"Editar exame ID {id_exame} (função ainda não implementada).")

    def baixar_exame(self, caminho_csv):
        try:
            destino, _ = QFileDialog.getSaveFileName(self, "Salvar como", caminho_csv)
            if destino:
                shutil.copy(caminho_csv, destino)
                QMessageBox.information(self, "Sucesso", "Arquivo salvo com sucesso.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo: {str(e)}")

    def excluir_exame(self, id_exame, caminho_csv):
        confirmar = QMessageBox.question(
            self, "Excluir", "Deseja realmente excluir este exame?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmar == QMessageBox.Yes:
            try:
                # Exclui o arquivo se ele existir
                if isinstance(caminho_csv, str) and os.path.isfile(caminho_csv):
                    os.remove(caminho_csv)

                # Remove do banco
                database.excluir_exame(id_exame)

                QMessageBox.information(self, "Excluído", "Exame excluído com sucesso.")
                self.carregar_exames()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao excluir exame: {str(e)}")

    def voltar(self):
        self.close()
        self.ante.show()