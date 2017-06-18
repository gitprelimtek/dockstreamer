FROM ubuntu:14.04

MAINTAINER Kaniu Ndungu

WORKDIR /

RUN  apt-get update

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip

RUN  apt-get update

RUN sudo  -H pip install --upgrade pip

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN git clone -b develop https://github.com/kaniutest/miner_web.git

WORKDIR /miner_web

EXPOSE 8080

CMD python server.py 
