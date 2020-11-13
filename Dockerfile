FROM python:3.6-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requeriments.txt

EXPOSE 3434

CMD [ "python" , "main.py" ]