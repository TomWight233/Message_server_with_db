FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the environment variable so Flask knows where the app is
ENV FLASK_APP=app.py
ENV APP_ENV=PRODUCTION
ENV PORT=5000

EXPOSE 5000

# Start the app using the standard Flask command
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]