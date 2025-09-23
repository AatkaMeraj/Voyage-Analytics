FROM python:3.9

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install waitress

ENV PORT 8080

# Use Waitress to serve the Flask app
CMD ["python", "-m", "waitress", "--host=0.0.0.0", "--port=8080", "flask_app:app"]
