FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements-local.txt /code/
RUN pip install -r requirements-local.txt
COPY . /code/
