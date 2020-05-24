 FROM python:3.7.6-buster
 
 RUN mkdir /sp_odesi_report_project/
 COPY ./requirements.txt /sp_odesi_report_project/
 COPY ./test-requirements.txt /sp_odesi_report_project/
 COPY . /sp_odesi_report_project/
 
 RUN pip install --upgrade pip
 # RUN pip install -e .
 RUN pip3 install -r /sp_odesi_report_project/test-requirements.txt
 
 WORKDIR /sp_odesi_report_project/
 RUN ls -alh
 RUN black tests
 
 CMD "pytest"
 ENV PYTHONDONTWRITEBYTECODE=true