#include "wifi_handler.h"

void wifi_task(void *pvParameters) {

  uint8_t status  = 0;
  uint8_t retries = 30;

  struct sdk_station_config config = {
    .ssid     = WIFI_SSID,
    .password = WIFI_PASS,
  };

  printf("INFO [wifi_task] Connecting to WiFi\n\r");
  sdk_wifi_set_opmode(STATION_MODE);
  sdk_wifi_station_set_config(&config);

  while (1) {

    while ((status != STATION_GOT_IP) && (retries)) {

      status = sdk_wifi_station_get_connect_status();

      printf("INFO [wifi_task] %s: status = %d\n\r", __func__, status );

      if (status == STATION_WRONG_PASSWORD) {
        printf("WARNING [wifi_task] WiFi: Wrong password\n\r");
        break;
      } else if (status == STATION_NO_AP_FOUND) {
        printf("WARNING [wifi_task] WiFi: AP not found\n\r");
        break;
      } else if (status == STATION_CONNECT_FAIL) {
        printf("WARNING [wifi_task] WiFi: Connection failed\r\n");
        break;
      }

      vTaskDelay(1000 / portTICK_PERIOD_MS);
      --retries;
    }

    if (status == STATION_GOT_IP) {
      printf("INFO [wifi_task] WiFi: Connected to (%s)\n\r", WIFI_SSID);
      xSemaphoreGive(wifi_alive);
      taskYIELD();
    }

    while ((status = sdk_wifi_station_get_connect_status()) == STATION_GOT_IP) {
      xSemaphoreGive(wifi_alive);
      taskYIELD();
    }

    printf("INFO [wifi_task] WiFi disconnected\n\r");
    sdk_wifi_station_disconnect();
    vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}
