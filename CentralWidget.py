from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries
from PyQt6.QtCore import Qt


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        series = QLineSeries()
        series.setName("Parabel")
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)

        axis_x = QValueAxis()
        axis_x.setTitleText("x-Achse")

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")

        q_chart = QChart()

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.setChart(q_chart)
