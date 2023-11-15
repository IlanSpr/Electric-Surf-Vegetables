FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=petzi_webhook.py
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "petzi_webhook:app"]
