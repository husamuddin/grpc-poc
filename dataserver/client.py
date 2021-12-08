import logging
import json
import grpc
import countries_pb2
import countries_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        request = json.dumps({
            "country": "egypt"
        })

        stub = countries_pb2_grpc.CountriesStub(channel)
        response = stub.GetCountries(
            countries_pb2.CountriesRequest(requestBody=request)
        )

        data = json.loads(
            response.data
        )

if __name__ == "__main__":
    logging.basicConfig()
    run()
