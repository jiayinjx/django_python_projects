FROM python:3.7.3-stretch

ARG DJANGO_VERSION=3.0.3
ARG DJANGO_HOME=/usr/local/django
ENV PROJECT_NAME=briderms

ADD resources/SHA256CAbundle.pem /opt/SHA256CAbundle.pem
ADD resources/pip.conf /etc/pip.conf
ADD resources/certs.py /opt/certs.py

# Installing Oracle instant clientdck
WORKDIR /opt/oracle
RUN apt-get update && apt-get install -y libaio1 wget unzip \
    && wget --no-check-certificate https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
    && unzip instantclient-basiclite-linuxx64.zip \
    && rm -f instantclient-basiclite-linuxx64.zip \
    && cd /opt/oracle/instantclient* \
    && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
    && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

WORKDIR ${DJANGO_HOME}/${PROJECT_NAME}
COPY ./${PROJECT_NAME} ${DJANGO_HOME}/${PROJECT_NAME}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python /opt/certs.py

EXPOSE 5656

RUN chmod +x ${DJANGO_HOME}/${PROJECT_NAME}/manage.py
RUN chmod +x ${DJANGO_HOME}/${PROJECT_NAME}/script/entrypoint.sh

CMD [ "python", "/usr/local/django/briderms/manage.py", "runserver", "0.0.0.0:5656" ]