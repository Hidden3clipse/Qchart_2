from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        series = QLineSeries()
        series.setName("Goldpreisentwicklung in €")
        #series.append(0, 0)
        series.append(QDateTime.fromString("2021-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1492.80)
        series.append(QDateTime.fromString("2022-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1698.03)
        series.append(QDateTime.fromString("2023-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1808.75)
        series.append(QDateTime.fromString("2024-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2391.22)

        axis_x = QDateTimeAxis()
        axis_x.setTitleText("Datum")

        start_date = QDateTime.fromString("2021-09-26", "yyyy-MM-dd")
        end_date = QDateTime.fromString("2024-09-26", "yyyy-MM-dd")

        axis_x.setRange(start_date, end_date)

        axis_x.setFormat("dd.MM.yyyy")

        axis_y = QValueAxis()
        axis_y.setTitleText("Goldpreis in €")
        axis_y.setRange(0, 2500)

        q_chart = QChart()
        q_chart.setTitle("Goldpreisentwicklung")

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.setChart(q_chart)
