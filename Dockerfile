FROM ubuntu:14.04
MAINTAINER Mark Spicer <mds4680@rit.edu>

# Disable tty.
ENV DEBIAN_FRONTEND noninteractive

# Get required packages.
RUN apt-get update
RUN apt-get install -y git python3-pip

# Install application.
ADD . /usr/local/openroast-api
RUN rm /usr/local/openroast-api/settings.ini
ADD production.ini /usr/local/openroast-api/settings.ini
WORKDIR /usr/local/openroast-api/
RUN python3 setup.py install

# Run application.
CMD gunicorn --bind 0.0.0.0:8000 openroast_api:app
