# esp32_library
Contains ESP32 projects. Based on https://github.com/espressif/ESP8266_RTOS_SDK

# Setup

## Get the Toolchain

The toolchain contains programs to compile and build the applications. I currently use version 5.2.0 for Linux 64:

https://dl.espressif.com/dl/xtensa-lx106-elf-linux64-1.22.0-100-ge567ec7-5.2.0.tar.gz

### ESP8266_RTOS_SDK

Included as submodule. It contains ESP8266 specific API / libraries.

## Environment Setup

```
# Install dependencies
sudo apt-get install git wget flex bison gperf python python-pip python-setuptools cmake ninja-build ccache libffi-dev libssl-dev

# The toolchain programs access ESP8266_RTOS_SDK using IDF_PATH environment variable.
export IDF_PATH=~/esp/ESP8266_RTOS_SDK

# Fix this yourself
/usr/bin/python -m pip install --user -r /home/erland/esp/ESP8266_RTOS_SDK/requirements.txt
```

## Clone esp32_library

```
git clone git@github.com:akerlund/esp32_library.git
cd esp32_library
git submodule update --init --recursive
```

## Build "Hello World"

```
cd submodules/examples/get-started/hello_world/
make menuconfig
```

Some weird GUI is supposed to start where you navigate to

```
Serial flasher config > Default serial port
```

Select your serial port, it can already be set to e.g.,

```
(/dev/ttyUSB0) Default serial port
```

