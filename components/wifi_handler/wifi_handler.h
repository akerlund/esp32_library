#ifndef WIFI_TASK_
#define WIFI_TASK_

#include "espressif/esp_common.h"
#include "FreeRTOS.h"
#include "task.h"

#include <espressif/esp_sta.h>
#include <espressif/esp_wifi.h>

#include <ssid_config.h>
#include <semphr.h>
#include <string.h>

extern SemaphoreHandle_t wifi_alive;
void wifi_task();

#endif
