FROM python

RUN pip install pymysql

ADD update_banner.py /

ENTRYPOINT [ "python", "/update_banner.py" ]
