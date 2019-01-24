FROM python:alpine

RUN apk update

RUN pip install --upgrade pip
RUN pip install pipenv

RUN mkdir -p /var/app
WORKDIR /var/app
COPY . /var/app

RUN pipenv install --system

ENV FLASK_APP app.py

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
