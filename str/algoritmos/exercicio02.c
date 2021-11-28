#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"


// define pinos de sensores
#define BOTAO_DESLIGA_LED 1;
#define SENSOR_PORTA_ENTRADA 2;
#define LED 3;
#define BUZZER 4;
#define SENSOR_TEMPERATURA 5;
#define SENSOR_FUMACA 6;
#define SENSOR_TENSAO 7;

// define limitar dos sensores
#define LIMIAR_TEMPERATURA 60;
#define LIMIAR_FUMACA 60;
#define LIMIAR_TENSAO 60;

// prototipos das funções
void xTaskSensorTemperatura (void *pvParameters);
void xTaskSensorFumaca (void *pvParameters);
void xTaskSensorTensao (void *pvParameters);
void xTaskEntradaDados (void *pvParameters);
void ligaBuzzerELed ();
void desligaBuzzer ();
void desligaLed ();
void resetPrints ();

// handler das tasks
TaskHandle_t taskSensorTemperatura = NULL;
TaskHandle_t taskSensorFumaca = NULL;
TaskHandle_t taskSensorTensao = NULL;
TaskHandle_t taskEntradaDados = NULL;

// instancia do mutex
SemaphoreHandle_t xSemaphoreMutex;

// controle de prints dos sensores
int temperatura_printado = 0;
int fumaca_printado = 0;
int tensao_printado = 0;

// setup inicial
void setup () {
  Serial.begin(9600);

  pinMode(BOTAO_DESLIGA_LED, INPUT);
  pinMode(SENSOR_PORTA_ENTRADA, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(SENSOR_TEMPERATURA, INPUT);
  pinMode(SENSOR_FUMACA, INPUT);
  pinMode(SENSOR_TENSAO, INPUT);

  xSemaphoreMutex = xSemaphoreCreateMutex();

  xTaskCreate(
    xTaskSensorTemperatura,
    "TASK_SENSORTEMPERATURA",
    configMINIMAL_STACK_SIZE + 64,
    ( void * ) 1,
    configMAX_PRIORITIES - 1,
    &taskSensorTemperatura
  );

  xTaskCreate(
    xTaskSensorFumaca,
    "TASK_SENSORFUMACA",
    configMINIMAL_STACK_SIZE + 64,
    ( void * ) 1,
    configMAX_PRIORITIES - 1,
    &taskSensorFumaca
  );

  xTaskCreate(
    xTaskSensorTensao,
    "TASK_SENSORTENSAO",
    configMINIMAL_STACK_SIZE + 64,
    ( void * ) 1,
    configMAX_PRIORITIES,
    &taskSensorTensao
  );

  xTaskCreate(
    xTaskEntradaDados,
    "TASK_ENTRADADADOS",
    configMINIMAL_STACK_SIZE + 128,
    ( void * ) 1,
    configMAX_PRIORITIES - 2,
    &taskEntradaDados
  );
}

// loop obrigatorio
void loop () {}

// funcao para efetuar o print na porta serial e  ligar o buzzer e o led
void ligaBuzzerELed (char nome[], int flag) {
  if(!flag) {
    Serial.println(String(nome) + " elevada");
  }
  if(digitalRead(BUZZER) === LOW) {
    digitalWrite(BUZZER, HIGH);
  }
  if(digitalRead(LED) === LOW) {
    digitalWrite(LED, HIGH);
  }
}

// função para desligar o buzzer
void desligaBuzzer () {
  digitalWrite(BUZZER, LOW);
}

// função para desligar o led
void desligaLed () {
  digitalWrite(BUZZER, LOW);
}

// função para resetar os prints dos sensores
void resetPrints () {
  temperatura_printado = 0;
  fumaca_printado = 0;
  tensao_printado = 0;
}

// task de monitoramento do sensor de temperatura
void xTaskSensorTemperatura (void *pvParameters) {
  BaseType_t  com_mutex;
  while(1) {
    if(digitalRead(SENSOR_TEMPERATURA >= LIMIAR_TEMPERATURA)) {
      com_mutex = xSemaphoreTake(xSemaphoreMutex,portMAX_DELAY);
      ligaBuzzerELed("Temperatura", temperatura_printado);
      temperatura_printado = 1;
    } else if (com_mutex == pdTRUE) {
      xSemaphoreGive(xSemaphoreMutex);
      desligaBuzzer();
      com_mutex = pdFALSE;
    }
    vTaskDelay(pdMS_TO_TICKS(500));
  }
}

// task de monitoramento do sensor de fumaça
void xTaskSensorFumaca (void *pvParameters) {
  BaseType_t  com_mutex;
  while(1) {
    if(digitalRead(SENSOR_FUMACA >= LIMIAR_FUMAÇA)) {
      com_mutex = xSemaphoreTake(xSemaphoreMutex,portMAX_DELAY);
      ligaBuzzerELed("Fumaca", temperatura_printado);
      fumaca_printado = 1;
      xSemaphoreGive(xSemaphoreMutex);
    } else if (com_mutex == pdTRUE) {
      xSemaphoreGive(xSemaphoreMutex);
      desligaBuzzer();
      com_mutex = pdFALSE;
    }
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}


// task de monitoramento do sensor de tensão
void xTaskSensorTensao (void *pvParameters) {
  BaseType_t  com_mutex;
  while(1) {
    if(digitalRead(SENSOR_TENSAO >= LIMIAR_TENSAO)) {
      com_mutex = xSemaphoreTake(xSemaphoreMutex,portMAX_DELAY);
      ligaBuzzerELed("Tensao", temperatura_printado);
      tensao_printado = 1;
      xSemaphoreGive(xSemaphoreMutex);
    } else if (com_mutex == pdTRUE) {
      xSemaphoreGive(xSemaphoreMutex);
      desligaBuzzer();
      com_mutex = pdFALSE;
    }
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}

// task de monitoramento do sensor da porta e botão de desligar o led
void xTaskEntradaDados (void *pvParameters) {
  while(1) {
    if(digitalRead(SENSOR_PORTA_ENTRADA) === HIGH) {
      xSemaphoreTake(xSemaphoreMutex, portMAX_DELAY);
      Serial.println("Porta aberta");
      xSemaphoreGive(xSemaphoreMutex);
    }

    if(digitalRead(BOTAO_DESLIGA_LED) === HIGH) {
      resetPrints();
      desligaLed();
    }
    vTaskDelay(pdMS_TO_TICKS(200));
  }
}
