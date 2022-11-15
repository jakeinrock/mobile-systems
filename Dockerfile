FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app

EXPOSE 8000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]