FROM python:3.11.3-alpine
WORKDIR /gh

COPY ["Pipfile","Pipfile.lock",".env","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy
        
COPY ["server.py","server_endpoint.py","./"]
EXPOSE 5000
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5000", "server_endpoint:app" ]