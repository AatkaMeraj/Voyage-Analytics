
FROM python:3.9-slim


WORKDIR /app


COPY . /app


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install waitress

ENV PORT=8080

CMD ["python", "-m", "waitress", "--port=8080", "flask_app:app"]
