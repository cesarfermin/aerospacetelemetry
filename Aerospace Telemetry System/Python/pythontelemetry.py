import sys
import serial
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QTimer
import pyqtgraph as pg

# ===== SERIAL =====
ser = serial.Serial('COM9', 9600)

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aerospace Telemetry & Control System")

        # ===== LABELS =====
        self.light_label = QLabel("Light: --")
        self.pot_label = QLabel("Throttle: --")
        self.alt_label = QLabel("Altitude: --")
        self.servo_label = QLabel("Servo: --")
        self.mode_label = QLabel("Mode: --")
        self.warning_label = QLabel("")

        # ===== STYLES =====
        self.warning_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px;")

        # ===== GRAPH =====
        self.graph = pg.PlotWidget()
        self.graph.setBackground("w")
        self.graph.setTitle("Live Altitude & Servo Response")

        self.alt_curve = self.graph.plot(pen='r', name="Altitude")
        self.servo_curve = self.graph.plot(pen='b', name="Servo")

        self.alt_data = []
        self.servo_data = []

        # ===== LAYOUT =====
        layout = QVBoxLayout()

        layout.addWidget(self.light_label)
        layout.addWidget(self.pot_label)
        layout.addWidget(self.alt_label)
        layout.addWidget(self.servo_label)
        layout.addWidget(self.mode_label)
        layout.addWidget(self.warning_label)
        layout.addWidget(self.graph)

        self.setLayout(layout)

        # ===== TIMER =====
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100)

    def update_data(self):
        try:
            line = ser.readline().decode().strip()
            parts = line.split(',')

            if len(parts) < 4:
                return

            # ===== PARSE =====
            light = int(parts[0].split(':')[1])
            pot = int(parts[1].split(':')[1])
            altitude = int(parts[2].split(':')[1])
            servo = int(parts[3].split(':')[1])

            # ===== CONTROL LOGIC (AUTO OVERRIDE) =====
            if altitude < 20:
                mode = "AUTO (SAFE)"
                servo_output = 90
                warning = "⚠ LOW ALTITUDE - AUTO CORRECTION ACTIVE"
            else:
                mode = "MANUAL"
                servo_output = servo
                warning = ""

            # ===== UPDATE LABELS =====
            self.light_label.setText(f"Light: {light}")
            self.pot_label.setText(f"Throttle: {pot}")
            self.alt_label.setText(f"Altitude: {altitude}")
            self.servo_label.setText(f"Servo: {servo_output}")
            self.mode_label.setText(f"Mode: {mode}")
            self.warning_label.setText(warning)

            # ===== COLOR STATUS =====
            if altitude < 20:
                self.alt_label.setStyleSheet("color: red; font-weight: bold;")
            else:
                self.alt_label.setStyleSheet("color: green;")

            # ===== STORE DATA =====
            self.alt_data.append(altitude)
            self.servo_data.append(servo_output)

            if len(self.alt_data) > 100:
                self.alt_data.pop(0)
                self.servo_data.pop(0)

            # ===== UPDATE GRAPH =====
            self.alt_curve.setData(self.alt_data)
            self.servo_curve.setData(self.servo_data)

        except:
            pass


app = QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec())