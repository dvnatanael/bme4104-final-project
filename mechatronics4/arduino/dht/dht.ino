#include "DHT.h"
#define dhtType DHT11

int const dhtPin = 8;

DHT dht;
float temperature;

void setup()
{
    Serial.begin(9600);
    dht = DHT(dhtPin, dhtType); // Initialize DHT sensor
    dht.begin();
}

void loop()
{
    temperature = dht.readTemperature();
    if (isnan(temperature))
    {
        Serial.println("Unable to read temperatue!");
    }
    else
    {
        Serial.print("Temperature: ");
        Serial.print(String(temperature));
        Serial.println("*C");
        delay(1000);
    }
}
