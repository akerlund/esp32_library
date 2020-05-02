# Component makefile for extras/chip_info

INC_DIRS += $(chip_info_ROOT)

# args for passing into compile rule generation
chip_info_SRC_DIR = $(chip_info_ROOT)

$(eval $(call component_compile_rules,chip_info))
