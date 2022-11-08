FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install -y \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY backend/ /code/backend
COPY py_scripts/ /code/

#RUN bash run.sh