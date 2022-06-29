#!/bin/sh


docker rm -f django-test
docker build -t django_test .
docker run -d -p 127.0.0.1:8005:8000 --name django-test  django_test