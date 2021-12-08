#!/usr/bin/sh

proto_files="\
countries.proto
"

for file in $proto_files;
do
  python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. $file
done;
