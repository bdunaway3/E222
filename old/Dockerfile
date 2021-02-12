FROM ubuntu:latest

MAINTAINER Tyler Balson "tbalson@iu.edu"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

ENV HOME /root
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

#ENTRYPOINT [ "python" ]
#ENTRYPOINT ["/bin/bash"]
#CMD ["server.py"]
CMD ["bash"]
