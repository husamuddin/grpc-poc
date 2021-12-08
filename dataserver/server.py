from country import list_countries as get_countries
from pprint import pprint
import json

from concurrent import futures
import logging

import grpc
import countries_pb2
import countries_pb2_grpc

class CountriesServicer(countries_pb2_grpc.CountriesServicer):
    def GetCountries(self, request, context):
        requesetBody = json.loads(request.requestBody)
        country = requesetBody['country']
        countries = get_countries(country)

        return countries_pb2.CountriesResponse(
           data  = json.dumps(countries)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    countries_pb2_grpc.add_CountriesServicer_to_server(CountriesServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("starting the gRPC server")
    logging.basicConfig()
    serve()
