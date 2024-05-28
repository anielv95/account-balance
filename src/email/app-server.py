from concurrent import futures
#import logging

import grpc
import email_pb2
import email_pb2_grpc
import server_email as s


class Greeter(email_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        result = s.send_email(request.data)
        return email_pb2.HelloReply(output=result)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
