FROM python:3.11.4-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN mkdir -p logs && pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . ./
CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]