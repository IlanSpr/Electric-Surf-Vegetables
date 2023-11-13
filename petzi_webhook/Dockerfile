FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV NAME World
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "petzi_webhook.wsgi:application"]
