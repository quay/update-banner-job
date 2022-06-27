FROM registry.access.redhat.com/ubi8/python-39:latest

RUN pip install pymysql

ADD update_banner.py /

ENTRYPOINT [ "python", "/update_banner.py" ]
