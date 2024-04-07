unsigned long lastButtonPressTime = 0;
const int buttonPin = 2; // the number of the pushbutton pin. PROBABLY CHANGE

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {    
    // reset the lastButtonPressTime
    lastButtonPressTime = millis();
  }

   // Check if 30 seconds have passed since the button was pressed
  if (millis() - lastButtonPressTime >= 30000 && lastButtonPressTime != 0) {
    // Reset the timer
    lastButtonPressTime = millis();
    // DO SOMETHING BLING BLING SCARA PAPA
  }

  if (Serial.available() > 0) {
    char received = Serial.read();
    
    // Echo the received byte back to the serial port. Uncomment if needed
    // Serial.print("Received: ");
    // Serial.println(received);
  }
}
