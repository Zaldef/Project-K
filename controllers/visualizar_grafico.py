from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import os

class VisualizarGraficos(QWidget):
    def __init__(self, exame_id):
        super().__init__()
        self.setWindowTitle(f"Gráfico do Exame {exame_id}")
        self.resize(800, 600)

        self.exame_id = exame_id
        self.layout = QVBoxLayout(self)

        self.canvas = FigureCanvas(Figure(figsize=(10, 5)))
        self.layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

        self.carregar_e_plotar_csv()

    def carregar_e_plotar_csv(self):
        try:
            # Monta o caminho com base no ID do exame
            filename = f"{self.exame_id}.xlsx"
            file_path = os.path.join("exames", "csvs", filename)

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Arquivo '{filename}' não encontrado.")

            # Lê os dados do Excel
            df = pd.read_excel(file_path, sheet_name='Raw Data')
            self.plotar_graficos(df)

        except Exception as e:
            QMessageBox.critical(self, "Erro ao carregar arquivo", str(e))

    def calcular_variacao_angulo(self, velocidade_angular, intervalos_tempo):
        rad_to_deg = 180 / np.pi
        return np.cumsum(velocidade_angular * intervalos_tempo) * rad_to_deg

    def plotar_graficos(self, df):
        # Calcula os intervalos de tempo
        time = df['Time (s)']
        time_intervals = np.diff(time, prepend=time.iloc[0])

        # Calcula as variações angulares
        angle_x = self.calcular_variacao_angulo(df['Gyroscope x (rad/s)'], time_intervals)
        angle_y = self.calcular_variacao_angulo(df['Gyroscope y (rad/s)'], time_intervals)
        angle_z = self.calcular_variacao_angulo(df['Gyroscope z (rad/s)'], time_intervals)

        # Limpa o canvas antes de desenhar
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        # Plota os três ângulos no mesmo gráfico
        ax.plot(time, angle_x, label='Ângulo X (deg)', color='r')
        ax.plot(time, angle_y, label='Ângulo Y (deg)', color='g')
        ax.plot(time, angle_z, label='Ângulo Z (deg)', color='b')

        ax.set_title("Variação de Ângulo nos Eixos X, Y e Z")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Ângulo (graus)")
        ax.legend()
        ax.grid(True)

        self.canvas.draw()
