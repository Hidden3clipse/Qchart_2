from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        series_euro = QLineSeries()
        series_euro.setName("Goldpreisentwicklung in €")
        series_euro.append(QDateTime.fromString("2021-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1492.80)
        series_euro.append(QDateTime.fromString("2021-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1590.60)
        series_euro.append(QDateTime.fromString("2022-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1781.90)
        series_euro.append(QDateTime.fromString("2022-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1731.28)
        series_euro.append(QDateTime.fromString("2022-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1690.30)
        series_euro.append(QDateTime.fromString("2022-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.45)
        series_euro.append(QDateTime.fromString("2023-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1838.68)
        series_euro.append(QDateTime.fromString("2023-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1763.45)
        series_euro.append(QDateTime.fromString("2023-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1808.75)
        series_euro.append(QDateTime.fromString("2023-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.45)
        series_euro.append(QDateTime.fromString("2024-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2004.30)
        series_euro.append(QDateTime.fromString("2024-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2164.99)
        series_euro.append(QDateTime.fromString("2024-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2386.69)

        series_dollar = QLineSeries()
        series_dollar.setName("Goldpreisentwicklung in $")
        series_dollar.append(QDateTime.fromString("2021-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1750.87)
        series_dollar.append(QDateTime.fromString("2021-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1788.48)
        series_dollar.append(QDateTime.fromString("2022-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1945.22)
        series_dollar.append(QDateTime.fromString("2022-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.54)
        series_dollar.append(QDateTime.fromString("2022-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1643.65)
        series_dollar.append(QDateTime.fromString("2022-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1750.40)
        series_dollar.append(QDateTime.fromString("2023-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1982.00)
        series_dollar.append(QDateTime.fromString("2023-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1913.73)
        series_dollar.append(QDateTime.fromString("2023-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1928.80)
        series_dollar.append(QDateTime.fromString("2023-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2002.39)
        series_dollar.append(QDateTime.fromString("2024-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2166.31)
        series_dollar.append(QDateTime.fromString("2024-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1913.73)
        series_dollar.append(QDateTime.fromString("2024-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2658.13)
        axis_x = QDateTimeAxis()
        axis_x.setTitleText("Datum")

        start_date = QDateTime.fromString("2021-09-26", "yyyy-MM-dd")
        end_date = QDateTime.fromString("2024-09-26", "yyyy-MM-dd")

        axis_x.setRange(start_date, end_date)

        axis_x.setFormat("dd.MM.yyyy")

        axis_euro = QValueAxis()
        axis_euro.setTitleText("Goldpreis in €")
        axis_euro.setRange(500, 3000)

        axis_dollar = QValueAxis()
        axis_dollar.setTitleText("Goldpreis in $")
        axis_dollar.setRange(500, 3000)

        q_chart = QChart()
        q_chart.setTitle("Goldpreisentwicklung")

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)
        q_chart.addAxis(axis_dollar, Qt.AlignmentFlag.AlignRight)

        q_chart.addSeries(series_euro)
        q_chart.addSeries(series_dollar)

        series_euro.attachAxis(axis_x)
        series_euro.attachAxis(axis_euro)

        series_dollar.attachAxis(axis_x)
        series_dollar.attachAxis(axis_dollar)

        self.setChart(q_chart)
