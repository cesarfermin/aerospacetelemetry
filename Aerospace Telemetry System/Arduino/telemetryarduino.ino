#include <Servo.h>

Servo myServo;

// Ultrasonic sensor pins
const int trigPin = 9;
const int echoPin = 10;

void setup() {
  Serial.begin(9600);

  // Ultrasonic setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Servo setup
  myServo.attach(6);
}

void loop() {

  // ===== READ LDR =====
  int lightValue = analogRead(A0);

  // ===== READ POTENTIOMETER =====
  int potValue = analogRead(A1);

  // ===== CONTROL SERVO =====
  int angle = map(potValue, 0, 1023, 0, 180);

  myServo.write(angle);

  // ===== ULTRASONIC SENSOR =====
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);

  int distance = duration * 0.034 / 2;

  // ===== SERIAL OUTPUT =====
  Serial.print("Light:");
  Serial.print(lightValue);

  Serial.print(",Pot:");
  Serial.print(potValue);

  Serial.print(",Altitude:");
  Serial.print(distance);

  Serial.print(",Servo:");
  Serial.println(angle);

  delay(100);
}