from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt


# Definiert die CentralWidget Klasse, die von QChartView erbt
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)  # Ruft den Konstruktor der Elternklasse auf

        # Erstellt eine Spline-Serie für das Diagramm
        series_spline = QSplineSeries()
        series_spline.setName("Hyperbel")  # Setzt den Namen der Serie auf "Hyperbel"

        # Fügt der Serie Punkte hinzu, die eine Hyperbel darstellen
        series_spline.append(-5, -0.2)
        series_spline.append(-4, -0.25)
        series_spline.append(-3, -0.33)
        series_spline.append(-2, -0.5)
        series_spline.append(-1, -1)
        series_spline.append(-0.01, -100)
        series_spline.append(0.01, 100)
        series_spline.append(1, 1)
        series_spline.append(2, 0.5)
        series_spline.append(3, 0.33)
        series_spline.append(4, 0.25)
        series_spline.append(5, 0.20)

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

        # Fügt die Spline-Serie dem Chart hinzu
        q_chart.addSeries(series_spline)

        # Verknüpft die Spline-Serie mit den Achsen
        series_spline.attachAxis(axis_x)
        series_spline.attachAxis(axis_y)

        # Setzt das Chart in das Chart-View Widget
        self.setChart(q_chart)
