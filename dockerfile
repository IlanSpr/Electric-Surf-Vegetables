FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN apt-get update && apt-get install -y gcc
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=petzi_webhook.py
CMD ["gunicorn", "--config", "gunicorn.conf.py", "petzi_webhook:app"]
