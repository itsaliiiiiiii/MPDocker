FROM nginx:alpine

FROM python:3.8-buster

LABEL maintainer="Ali Harit <ali.harit@usms.ac.ma>"

RUN apt-get update && apt-get install -y libldap2-dev libsasl2-dev python3-dev

WORKDIR /

COPY student_age.py /
COPY student_age.json /data/student_age.json
COPY requirements.txt /

RUN pip3 install -r /requirements.txt

VOLUME /data

EXPOSE 3000

CMD ["python3", "./student_age.py"]
