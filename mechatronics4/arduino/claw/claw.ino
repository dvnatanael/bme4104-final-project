#include <Servo.h>

int const servoPin = 9;

Servo myServo;
String command;

void setup()
{
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop()
{
    if (Serial.available())
    {
        command = Serial.readStringUntil('\n');
        Serial.println(command);

        if (command == "open")
        {
            myServo.write(40);
            delay(1000);
        }
        else if (command == "close")
        {
            myServo.write(0);
            delay(1000);
        }
    }
}
