#include <stdio.h>
#include "espressif/esp_common.h"

#include "chip_info.h"

void print_chip_info() {

  printf("\n");
  printf("SDK version : %s\n", sdk_system_get_sdk_version());
  printf("GIT version : %s\n", GITSHORTREV);

}
