FROM python:alpine

WORKDIR /opt/local-otp

COPY src/ .

RUN python setup.py install

ENTRYPOINT ["/usr/local/bin/lotp"]
