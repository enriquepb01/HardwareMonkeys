/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>
#include <LiquidCrystal.h>
#define BUTTON_PIN 4

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

LiquidCrystal lcd(12, 11, 8, 7, 5, 3);

int pos = 90;    // variable to store the servo position
const int buzzer = 10;
int rewardState = 0;
unsigned long lastButtonPressTime = 0;
unsigned long playTime;
char receivedInfo = 0;
char receivedData;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(buzzer, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  lcd.begin(16, 2);
  // lcd.print("OOOOHHH OOOHHH AHH AHHH!");
  Serial.begin(9600);
  playTime = millis() + 600000;
}

void loop() {
  lcd.setCursor(0, 1);
  lcd.print((playTime - millis()) / 1000); // print how much time left in game
  lcd.setCursor(1,1);
  lcd.print((millis() - lastButtonPressTime) / 1000); // count up to 30.

  byte press = digitalRead(BUTTON_PIN);

  if(press == LOW){
    lastButtonPressTime = millis();
  }

  if (millis() - lastButtonPressTime >= 30000 && lastButtonPressTime != 0) {
    // Reset the timer
    lastButtonPressTime = millis();
    rewardState = 2;
  }

  if (receivedInfo && receivedData == 1) {
    rewardState = 1;
  } else if (receivedInfo && receivedData == 2) {
    rewardState = 2;
  } else if (receivedInfo && receivedData == 3) {
    rewardState = 3;
  }
  

  if(rewardState == 1){
  tone(buzzer, 440);
  delay(250);
  noTone(buzzer);
  tone(buzzer, 660);
  delay(250);
  noTone(buzzer);
  tone(buzzer, 880);
  delay(250);
  noTone(buzzer);
  tone(buzzer, 1100);
  delay(500);
  noTone(buzzer);
  rewardState = 0;
  }

  if(rewardState == 2){
    tone(buzzer, 90);
  delay(1000);
  noTone(buzzer);
  rewardState = 0;
  }

  if(rewardState == 3){
  for (pos = 90; pos >= 40; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 40; pos <= 90; pos += 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    }
    rewardState = 0;
  }

  if (Serial.available() > 0) {
    receivedData = Serial.read();
    receivedInfo = 1;
    lcd.setCursor(0, 1);
    lcd.print(receivedData);
    lcd.print("GOTCHU");
    delay(1000);
  }
}
