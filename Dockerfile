FROM ubuntu:16.04
MAINTAINER Jeffrey Lim "jeffrey@cloa.io"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
RUN git clone https://github.com/cloatech/status-worker_main.git
COPY . /worker_main
WORKDIR /worker_main
RUN pip install -r requirements.txt
CMD ["worker_main.py"]