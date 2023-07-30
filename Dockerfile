FROM python:3.11.4-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV HOST=ikura-db
ENV FLASK_APP=app.py
ENV SK=ikurawebapp
EXPOSE 5000
COPY app .
CMD ["waitress-serve", "--listen=*:5000", "app:app"]
# CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
