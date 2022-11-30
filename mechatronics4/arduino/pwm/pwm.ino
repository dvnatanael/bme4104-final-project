const int In1 = 5; // left wheel
const int In2 = 6;
const int In3 = 10; // right wheel
const int In4 = 11;

void setup()
{
    pinMode(In1, OUTPUT);
    pinMode(In2, OUTPUT);
    pinMode(In3, OUTPUT);
    pinMode(In4, OUTPUT);
}

void loop()
{
    move_forward();
    delay(2000);

    stop();
    delay(500);

    move_backward();
    delay(2000);

    stop();
    delay(500);
}

void stop()
{
    analogWrite(In1, 0);
    analogWrite(In2, 0);
    analogWrite(In3, 0);
    analogWrite(In4, 0);
}

void move_forward()
{
    analogWrite(In1, 50);
    analogWrite(In2, 0);
    analogWrite(In3, 50);
    analogWrite(In4, 0);
}

void move_backward()
{
    analogWrite(In1, 0);
    analogWrite(In2, 50);
    analogWrite(In3, 0);
    analogWrite(In4, 50);
}
