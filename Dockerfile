FROM frolvlad/alpine-python3
MAINTAINER Jeffrey Lim "jeffrey@cloa.io"
RUN apk add --no-cache git
RUN git clone https://github.com/jsrimr/flask-signal-worker.git
COPY . /worker_main
WORKDIR /worker_main
RUN pip3 install -r /worker_main/requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]