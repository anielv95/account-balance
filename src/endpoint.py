from __future__ import print_function

from flask import Flask
from flask import request
from flask import jsonify
import processing as p

import grpc
import email_pb2
import email_pb2_grpc
import os

app = Flask("processing")


@app.route("/processing", methods=["POST"])
def predict():
    customer = request.get_json()

    result = p.calculate_values(customer["account"], customer["email"], customer["df"])
    host = os.getenv("EMAIL_HOST", "localhost:50051")
    with grpc.insecure_channel(host) as channel:
        stub = email_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(email_pb2.HelloRequest(data=result))
        print(response.output)

    return jsonify({"status": "Email was sent"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
