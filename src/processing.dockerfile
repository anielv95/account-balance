FROM python:3.11.3-alpine
WORKDIR /gh

COPY ["Pipfile","Pipfile.lock","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy
        
COPY ["processing.py","endpoint.py","email_pb2.py","email_pb2_grpc.py","./"]
EXPOSE 3000
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:3000", "endpoint:app" ]