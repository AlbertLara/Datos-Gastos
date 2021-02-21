FROM python:3.8

WORKDIR /app
ARG PORT=$PORT

ENV PORT $PORT

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# copy services
COPY . /app