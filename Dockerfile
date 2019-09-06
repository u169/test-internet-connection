FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
COPY arguments.py /app
COPY main.py /app

RUN ls

RUN pip install -r requirements.txt

CMD python main.py --repeat 500 --url http://httpbin.org/json