from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt6.QtCore import Qt

# Die Klasse CentralWidget erbt von QChartView, das für die Darstellung eines Charts verwendet wird
class CentralWidget(QChartView):
    def __init__(self, parent=None):  # Konstruktor der Klasse
        super(CentralWidget, self).__init__(parent)  # Ruft den Konstruktor der Basisklasse QChartView auf

        # Erstelle eine QLineSeries für die Parabel
        series = QLineSeries()
        series.setName("Parabel als QLineSeries")  # Setze den Namen der Serie
        series.append(0, 0)  # Füge den Punkt (0, 0) hinzu
        series.append(1, 1)  # Füge den Punkt (1, 1) hinzu
        series.append(2, 4)  # Füge den Punkt (2, 4) hinzu
        series.append(3, 9)  # Füge den Punkt (3, 9) hinzu

        # Erstelle eine QSplineSeries für die Parabel (weiche Linienkurve)
        series_spline = QSplineSeries()
        series_spline.setName("Parabel als QSplineSeries")  # Setze den Namen der Splineserie
        series_spline.append(0, 0)  # Füge den Punkt (0, 0) hinzu
        series_spline.append(1, 1)  # Füge den Punkt (1, 1) hinzu
        series_spline.append(2, 4)  # Füge den Punkt (2, 4) hinzu
        series_spline.append(3, 9)  # Füge den Punkt (3, 9) hinzu

        # Erstelle eine x-Achse
        axis_x = QValueAxis()
        axis_x.setTitleText("x-Achse")  # Setze den Titel der x-Achse

        # Erstelle eine y-Achse
        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")  # Setze den Titel der y-Achse

        # Erstelle ein QChart-Objekt, das die Darstellung der Daten übernimmt
        q_chart = QChart()

        # Füge die x-Achse zum Chart hinzu, und richte sie unten aus
        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        # Füge die y-Achse zum Chart hinzu, und richte sie links aus
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        # Füge die lineare Serie (QLineSeries) dem Chart hinzu
        q_chart.addSeries(series)
        # Füge die spline Serie (QSplineSeries) dem Chart hinzu
        q_chart.addSeries(series_spline)

        # Verknüpfe die x-Achse mit der QLineSeries
        series.attachAxis(axis_x)
        # Verknüpfe die y-Achse mit der QLineSeries
        series.attachAxis(axis_y)

        # Verknüpfe die x-Achse mit der QSplineSeries
        series_spline.attachAxis(axis_x)
        # Verknüpfe die y-Achse mit der QSplineSeries
        series_spline.attachAxis(axis_y)

        # Setze das QChart-Objekt in der Ansicht (QChartView)
        self.setChart(q_chart)
