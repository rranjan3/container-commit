FROM python:3

RUN mkdir /project

ADD test_commit.py /project

WORKDIR /project
