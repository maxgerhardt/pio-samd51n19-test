#include <Arduino.h>

/* look into variant.cpp to know what MCU pin this maps to */
/* this one is custom added for PA00 */
#define LED_PIN 97

void setup() {
    pinMode(LED_PIN, OUTPUT);
}
void loop() {
    digitalWrite(LED_PIN, LOW);
    delay(1000);
    digitalWrite(LED_PIN, HIGH);
    delay(1000);
}
