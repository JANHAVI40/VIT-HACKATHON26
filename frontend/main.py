import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys
sys.path.append("../backend")

from sniffer import start_sniffer, register_callback


class Dashboard(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI SOC Dashboard")
        self.setGeometry(200,200,900,500)

        self.table = QTableWidget()
        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Attacker IP",
            "Target IP",
            "Protocol",
            "Port",
            "Stage",
            "Risk"
        ])

        self.setCentralWidget(self.table)

        register_callback(self.update_dashboard)

        start_sniffer()

    def update_dashboard(self,data):

        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row,0,QTableWidgetItem(data["src_ip"]))
        self.table.setItem(row,1,QTableWidgetItem(data["dst_ip"]))
        self.table.setItem(row,2,QTableWidgetItem(data["protocol"]))
        self.table.setItem(row,3,QTableWidgetItem(str(data["dst_port"])))
        self.table.setItem(row,4,QTableWidgetItem(data["stage"]))
        self.table.setItem(row,5,QTableWidgetItem(str(data["risk"])))


app = QApplication(sys.argv)

window = Dashboard()
window.show()

sys.exit(app.exec())