int const buzzer = 6;
int const echo = 12;
int const trigger = 13;

int duration;
float distance;

void setup()
{
    Serial.begin(9600);

    pinMode(buzzer, OUTPUT);
    pinMode(echo, INPUT);
    pinMode(trigger, OUTPUT);
}

void loop()
{
    // send a ~10 us pulse to trigger the ultrasonic sensor
    digitalWrite(trigger, LOW);
    delayMicroseconds(1);
    digitalWrite(trigger, HIGH);
    delayMicroseconds(11);
    digitalWrite(trigger, LOW);

    // read the duration of reflected pulse
    duration = pulseIn(echo, HIGH);

    if (duration > 0)
    {
        // speed of sound in air is ~340m/s = 34000cm/s = 0.034cm/us
        distance = 0.0340 *  duration / 2;
        Serial.println(distance);

        if (distance < 5)
        {
            tone(buzzer, 200, 1000);
            delay(2000);
        }
    }
}
