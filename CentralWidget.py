import math  # Importiert das Mathematikmodul, das jedoch hier nicht verwendet wird

from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt6.QtCore import Qt

# Definiert die CentralWidget Klasse, die von QChartView erbt
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)  # Ruft den Konstruktor der Elternklasse auf

        # Setzt den Abstand zwischen den X-Werten auf 0.1
        delta_x = 0.1

        # Definiert den Bereich der X-Achse
        x_min = -2.5
        x_max = 3.0

        # Berechnet Start- und Endwerte für die Schleife
        start = int(x_min / delta_x)
        end = int(x_max / delta_x)

        # Erstellt eine Liste von X-Werten in Schritten von delta_x
        values_x = [i * delta_x for i in range(start, end)]

        # Berechnet die Y-Werte für das Polynom und speichert sie in einer Liste
        values_sine = []
        for x in values_x:
            values_sine.append(x**3 - 2 * x**2 + 4 * x - 3)

        # Erstellt eine Linien-Serie
        series_sinus = QLineSeries()
        series_sinus.setName("Polynom")  # Setzt den Namen der Serie auf "Polynom"

        # Fügt der Serie die X- und Y-Werte hinzu
        for i in range(len(values_x)):
            series_sinus.append(values_x[i], values_sine[i])

        # Erstellt und konfiguriert die X-Achse
        axis_x = QValueAxis()
        axis_x.setRange(x_min, x_max)  # Setzt den Bereich der X-Achse
        axis_x.setTitleText("x-Achse")  # Setzt den Titel der X-Achse

        # Erstellt und konfiguriert die Y-Achse
        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")  # Setzt den Titel der Y-Achse

        # Erstellt das Chart-Objekt
        q_chart = QChart()

        # Fügt die Achsen dem Chart hinzu
        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)  # X-Achse unten
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)    # Y-Achse links

        # Fügt die Linie (Polynom-Serie) dem Chart hinzu
        q_chart.addSeries(series_sinus)

        # Verknüpft die Serie mit den Achsen
        series_sinus.attachAxis(axis_x)
        series_sinus.attachAxis(axis_y)

        # Setzt das Chart in das Chart-View Widget
        self.setChart(q_chart)
