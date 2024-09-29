from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries
from PyQt6.QtCore import Qt


# Definiert die CentralWidget Klasse, die von QChartView erbt
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)  # Ruft den Konstruktor der Elternklasse QChartView auf

        # Erstellt eine Linien-Serie für das Diagramm
        series = QLineSeries()
        series.setName("Parabel")  # Setzt den Namen der Serie auf "Parabel"

        # Fügt der Serie Punkte hinzu, die eine Parabel darstellen (y = x^2)
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)

        # Erstellt und konfiguriert die X-Achse
        axis_x = QValueAxis()
        axis_x.setTitleText("x-Achse")  # Setzt den Titel der X-Achse

        # Erstellt und konfiguriert die Y-Achse
        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")  # Setzt den Titel der Y-Achse

        # Erstellt das Chart-Objekt
        q_chart = QChart()

        # Fügt die Achsen dem Chart hinzu
        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)  # X-Achse unten
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)  # Y-Achse links

        # Fügt die Serie dem Chart hinzu
        q_chart.addSeries(series)

        # Verknüpft die Serie mit den Achsen
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        # Setzt das Chart in das Chart-View Widget
        self.setChart(q_chart)
