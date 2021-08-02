FROM python:3.8-slim-buster
ADD ./input ./input
ADD ./output ./output

COPY main.py ./
COPY requirements.txt ./

RUN pwd
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT ["python3","main.py"]
