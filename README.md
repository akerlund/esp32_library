# esp_library

This repository contains projects for the ESP WiFi module that are based on https://github.com/SuperHouse/esp-open-rtos.

The projects are in their own repositories and are included here as submodules. In order to pull down everything simply follow the following numbered steps.

## 1 Clone Repository

The repository has several submodules which in turn also have submodules, hence you need to use the *--recursive* flag when you clone.

```
git clone --recursive https://github.com/akerlund/esp32_library
```

## 3 Get the Toolchain

Easy step would be to download the Linux 64 v5.2.0 from [here](https://dl.espressif.com/dl/xtensa-lx106-elf-linux64-1.22.0-100-ge567ec7-5.2.0.tar.gz). There are some instruction about how you can build **esp-open-sdk** yourself further down in this document. Place the extracted files in your desired folder. Include it in your path, for example

```bash
export PATH=$PATH:/home/erland/Documents/esp-open-sdk/xtensa-lx106-elf/bin
```

This will only be valid in the virtual terminal you are currently working in. You can add it to your **.bashrc** file (in your home folder) so the path is visible in all new terminals.

## 4 Install esp-tool

A Python-based, open source, platform independent, utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32 chips.

```
sudo pip install esptool
sudo pip3 install esptool
```

Make sure your user is added to the **dialout** group with

```
groups
```

because otherwise you cannot use the serial port. If you do not see **dialout** then do

```
sudo adduser your_user_name dialout
```

You must now log in and out again for it to take effect.

## 2 Setup Your WiFi Password

To build any examples that use WiFi, create in the cloned folder

```
submodules/esp-open-rtos/include/private_ssid_config.h
```

and then define the two macros for your SSID and password to your WiFi network:

```c
#define WIFI_SSID "mywifissid"
#define WIFI_PASS "my secret password"
```

## 3 Now make a test

```
make flash -j4 -C examples/mqtt_client
```

# Setup of the Mosquitto MQTT Broker

Install is easy

```
sudo apt install mosquitto
```

Setup UFW - Uncomplicated Firewall

```
sudo ufw allow 1883
sudo ufw enable
```

Verify UFW
```
sudo ufw status
```

Verify TCP port 1883

```
netstat -ltpn | grep 1883
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 0.0.0.0:1883            0.0.0.0:*               LISTEN      -
tcp6       0      0 :::1883                 :::*                    LISTEN      -
```

Observe the ESP's serial output

```
screen /dev/ttyUSB0 115200
```

# Visual Studio Code
## Configure include path
Add these lines under the Include path section in the VS Code C/C++ extension so it knows where to look for the header files used in the hello_world example project:
```
~/esp/ESP8266_RTOS_SDK/components/**
~/esp/ESP8266_RTOS_SDK/components/freertos/**
~/esp/ESP8266_RTOS_SDK/components/freertos/port/esp8266/include/
```

# Manual build of esp-open-sdk

Install a lot of prerequisites:

```
sudo sudo apt-get install make unrar-free autoconf automake libtool gcc g++ gperf flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial sed git unzip bash help2man wget bzip2 libtool-bin

git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
```

My bash is too new so I had to change line 193 at: esp-open-sdk/crosstool-NG/configure.ac
like this:

```bash
|$EGREP '^GNU bash, version ([0-9\.]+)')
```

Then I could build


```bash
cd esp-open-sdk
make toolchain esptool libhal STANDALONE=n
```

which took for ever but then I added the path to the /bin

```bash
export PATH=$PATH:/home/erland/Documents/esp-open-sdk/xtensa-lx106-elf/bin
```

