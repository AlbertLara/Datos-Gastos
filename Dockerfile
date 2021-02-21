FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY /app/ /app

WORKDIR /app

RUN pip install -r requirements.txt
# copy services

RUN ls / -Rl

ENTRYPOINT ["python"]

CMD ["main.py"]