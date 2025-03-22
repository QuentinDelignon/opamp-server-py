python -m grpc_tools.protoc -I. --protobuf-to-pydantic_out=../opamp_server_py/types opamp.proto
python -m grpc_tools.protoc -I. --protobuf-to-pydantic_out=../opamp_server_py/types anyvalue.proto