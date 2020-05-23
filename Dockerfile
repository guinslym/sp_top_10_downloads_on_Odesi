FROM python:3.7.6-buster
MAINTAINER guinslym

RUN mkdir /sp_odesi_report_project/
COPY ./test-requirements.txt /sp_odesi_report_project/
# COPY . .

RUN pip install --upgrade pip
# RUN pip install -e .
RUN pip3 install -r /sp_odesi_report_project/test-requirements.txt

WORKDIR /sp_odesi_report_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
