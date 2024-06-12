FROM python:3.11.3-alpine
WORKDIR /gh

COPY ["Pipfile","Pipfile.lock",".env","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy
        
COPY ["server_email.py","app-server.py","email_pb2.py","email_pb2_grpc.py","./"]
EXPOSE 50051
ENTRYPOINT [ "python", "app-server.py" ]