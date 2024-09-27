from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        series_spline = QSplineSeries()
        series_spline.setName("Hyperbel")
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

        axis_x = QValueAxis()
        axis_x.setTitleText("x-Achse")

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")

        q_chart = QChart()

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series_spline)

        series_spline.attachAxis(axis_x)
        series_spline.attachAxis(axis_y)

        self.setChart(q_chart)
