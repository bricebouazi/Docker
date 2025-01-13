FROM debian:oldstable-20241202
Run apt-get update
&& apt-get install python:2.7.13-slim
LABEL org.opencontainers.image.authors="bbouazi@yahoo.fr"
ADD *.py /
EXPOSE 6000
CMD["python","./main.py"]
