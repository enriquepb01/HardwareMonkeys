void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();
    
    // Echo the received byte back to the serial port. Uncomment if needed
    // Serial.print("Received: ");
    // Serial.println(received);
  }
}
