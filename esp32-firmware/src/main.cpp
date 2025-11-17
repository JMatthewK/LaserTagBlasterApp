#include <Arduino.h>

#define LED_PIN 2   // Built-in blue LED on most ESP32-WROOM boards

void setup() {
    pinMode(LED_PIN, OUTPUT);  // Set LED pin as output
}

void loop() {
    digitalWrite(LED_PIN, HIGH);  // LED ON
    delay(500);                   // half a second
    digitalWrite(LED_PIN, LOW);   // LED OFF
    delay(2000);                   // 2 second
}
