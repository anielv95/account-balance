# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC email.Greeter server."""

from concurrent import futures
import logging

import grpc
import email_pb2
import email_pb2_grpc
import server_email as s


class Greeter(email_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        result = s.send_email(request.data)
        return email_pb2.HelloReply(output=result)

    # def SayHelloAgain(self, request, context):
    #     return email_pb2.HelloReply(message="Hello again, %s!" % request.name)


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
