FROM python:3.10-alpine
WORKDIR /home/sardor/python
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    python3-dev \
    py3-pip \
    build-base \
    && pip install --upgrade pip
COPY  ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src /home/sardor/python/src
COPY ./test /home/sardor/python/test
RUN ls -l /home/sardor/python/src


CMD ["python3", "-m", "test.main", "test_files/test_xml.xml"]
#CMD sh
