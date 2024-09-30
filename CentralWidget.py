from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        series = QLineSeries()
        series.setName("Goldpreisentwicklung in €")
        series.append(0, 0)
        series.append(1, 1492.80)
        series.append(2, 1698.03)
        series.append(3, 1808.75)
        series.append(4, 2391.22)

        axis_x = QDateTimeAxis()
        axis_x.setTitleText("Datum")


        start_date = QDateTime.fromString("2021-09-26", "yyyy-MM-dd", 0)
        end_date = QDateTime.fromString("2024-09-26", "yyyy-MM-dd", 0)

        start_date = add_milliseconds("2021-09-26", "00:00:00", 0)
        end_date = add_milliseconds("2024-09-26", "00:00:00", 0)

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
