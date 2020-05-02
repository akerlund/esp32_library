# Component makefile for extras/buffer

INC_DIRS += $(buffer_ROOT)

# args for passing into compile rule generation
buffer_SRC_DIR = $(buffer_ROOT)

$(eval $(call component_compile_rules,buffer))
