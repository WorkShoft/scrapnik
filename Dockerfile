FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements-local.txt /code/
RUN pip install -r requirements-local.txt
COPY . /code/
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s /usr/local/bin/docker-entrypoint.sh / # backwards compat
# NodeJS is needed as a backend for cloudflare-bypassing packages
RUN apt update && apt install -y --no-install-recommends apt-utils
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt install -y nodejs

