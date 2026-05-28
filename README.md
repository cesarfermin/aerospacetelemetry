# Aerospace Telemetry System w/ Python and Arduino

Real-time telemetry system built with Python and Arduino. This project shows the basics of aerospace monitoring, specifically actuator control with a live GUI dashboard, sensors and altitude tracking. 


# Overview 

This project shows a rather simplified aerospace telemetry system that demonstrates real-time sensor data from an Arduino to a Python dashboard. It visualizes different components such as light, throttle, altitude levels and servo response while containing a safety override loop if altitude levels are dangerously low. This is a representation of the integration of embedded systems and control logic often used in aerospace systems. 


# Features

- Servo motor monitoring
- Real-time updates with GUI and live graphing
- Automatic safety override if altitude levels are dangerously low
- Manual vs Auto control modes
- Live dashboard using PyQt6
- Multiple Sensors:
  LDR (Light levels)
  Potentiometer (Throttle)
  Ultrasonic Sensor (Altitude simulator)
- Plotting of servo response and altitude using PyQtGraph

# Control

- MANUAL MODE:
  Servo motor's position follows potentiometer directly.
- AUTO SAFE MODE:
  If altitude levels drop dangerously low, the system will automatically override the servo motor's position to a safe angle.

  The python dashboard monitors altitude levels in real-time to determine which mode should be active.


# Technology Used

- Python 3
- PyQtGraph
- PySerial
- Arduino (C++)
- PyQt6


# Hardware Used

- Arduino Uno (Elegoo Uno)
- Light Dependent Resistor
- Servo Motor
- Potentiometer
- HC-SR04 Ultrasonic Sensor

# Live Dashboard

The python dashboard displays the following:

- Light levels
- Throttle
- System mode (Manual or Auto)
- Real-time altitude levels and servo position graph
- Servo motor angle
- Altitude in CM


# How to Run

1. Install Python
2. Upload Arduino code
   

 RUN ->  Arduino/telemetryarduino.ino

3. Run the Python Dashboard

  RUN -> py Python/pythontelemetry.py

   Assure the correct COM port is selected. 
   

# Future Telemetry System Improvements

- Wireless telemetry of some kind
- Expanded telemetry diagnostics
- Kalman filtering
- CSV data logging


# Author 

**Cesar Fermin**
Mechanical Engineering Student
University of Wisconsin-Madison
