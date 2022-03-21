FROM python:2-alpine as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /
RUN pip install --no-warn-script-location --prefix=/install -r /requirements.txt

FROM base
STOPSIGNAL SIGINT
COPY --from=builder /install /usr/local
COPY src /app
WORKDIR /app

CMD [ "python", "-u", "/app/aidon_mqtt.py" ]
