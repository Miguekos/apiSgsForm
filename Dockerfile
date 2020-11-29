FROM python:3.6-alpine

WORKDIR /app

COPY [ "./requeriments.txt" , "/app" ]

RUN pip install -r requeriments.txt

COPY . /app

EXPOSE 3434

CMD [ "python" , "main.py" ]