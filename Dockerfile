FROM python:3.9

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

ENV PORT 8080

CMD ["gunicorn", "app:app", "--config=config.py"]
