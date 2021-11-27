// ----------------
// O Contador sera incrementado enquanto o programa estiver
// rodando, assim não é possivel determinar seu valor final
// ----------------

#include "freertos/FreeRTOS.h"
#include "freertos/timers.h"

#define LED 13

void xCallbackInverteValorLed();
void xCallbackDesligaLed();

int contador = 0;

void setup () {
    Serial.begin(9600);
    pinMode(LED,OUTPUT);

    xTimerInverteLed = xTimerCreate("xTimerInverteLed",pdMS_TO_TICKS(250),pdTRUE,( void * ) 0,xCallbackInverteValorLed);
    xTimerDesligaLed = xTimerCreate("xTimerDesligaLed",pdMS_TO_TICKS(5000),pdFALSE,( void * ) 0,xCallbackDesligaLed);

    xTimerStart(xTimerInverteLed,0);
    xTimerStart(xTimerDesligaLed,pdMS_TO_TICKS(5000));
}

void loop {}

void xCallbackInverteValorLed () {
    digitalWrite(LED, !digitalRead(LED));
    counter++;
    Serial.println(String(contador));
}

void xCallbackDesligaLed () {
    digitalWrite(LED,LOW);
    Serial.println("DESLIGANDO");
}
