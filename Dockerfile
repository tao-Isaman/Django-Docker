FROM python:3.9.0a5-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code/
WORKDIR /code/odds_work
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
