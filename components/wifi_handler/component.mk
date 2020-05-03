# Component makefile for wifi_handler

INC_DIRS += $(wifi_handler_ROOT)

# args for passing into compile rule generation
wifi_handler_SRC_DIR = $(wifi_handler_ROOT)

$(eval $(call component_compile_rules,wifi_handler))
