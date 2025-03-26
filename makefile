# Makefile for updating gRPC schemas

# Variables
PROTO_DIR = specs
OUTPUT_DIR = opamp_server_py/types
PROTO_FILES = opamp.proto anyvalue.proto

# Default target
.PHONY: all

all: schemas

# Target to update schemas using grpc_tools.protoc
schemas:
	poetry run python -m grpc_tools.protoc \
		-I $(PROTO_DIR) \
		--python_betterproto_opt=typing.310 \
		--python_betterproto_opt=pydantic_dataclasses \
		--python_betterproto_out=$(OUTPUT_DIR) \
		$(PROTO_FILES)