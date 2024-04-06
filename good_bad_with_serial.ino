/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position
const int buzzer = 10;
char received = 0;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if(Serial.available() > 0){
    received = Serial.read();
  }

 // Positive
  if(received == 1){
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
  received = 0;
  }

  // Negative
  if(received == 2){
    tone(buzzer, 90);
  delay(1000);
  noTone(buzzer);
  received = 0;
  }

  // Checkmate
  if(received == 3){
  for (pos = 90; pos >= 40; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 40; pos <= 90; pos += 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    }
    received = 0;
  }
}
