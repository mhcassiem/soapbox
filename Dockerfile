# syntax=docker/dockerfile:1

FROM python:slim-bullseye

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app
RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

#CMD [ "gunicorn", "--graceful-timeout", "5" , "wsgi:app", "-w", "4", "-b", "0.0.0.0:8000"]