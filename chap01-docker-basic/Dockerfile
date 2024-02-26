FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y \
      curl \
      python3-dev

WORKDIR /root
COPY hello.py .
ENV MY_VER 2.0.0

CMD ["python3", "hello.py", "Guest"]

